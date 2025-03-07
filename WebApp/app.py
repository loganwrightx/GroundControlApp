import dash
from dash import Dash, html, dcc, Input, Output, callback
import serial
import time

from utils.operating_modes import *
from utils.commands import *

om = OperatingMode(0)

try:
  ser = serial.Serial(port="/dev/tty.usbmodem101", baudrate=115200)
except serial.serialutil.SerialException as E:
  print(f"Encountered a problem: {E.strerror}")
  print("Check connections and restart the app.")
  exit(0)

app = Dash(__name__, suppress_callback_exceptions=True, assets_folder="./assets")

incoming_packet: list = ["" for _ in range(6)]
REFRESH_RATE: int = 50

app.layout = html.Div([
  dcc.Location(id="url", refresh=False),
  html.Title(children="Ground Control"),
  html.Div(id="blank-container", className="blank-container"),
  html.H1("Ground Control", style={"display": "flex", "width": "100vw", "align-items": "center"}),
  html.Div([
    html.Button(commands[i], id=f"command-{i}", className="command-button") for i in range(len(Commands))
  ], className="command-buttons-container"),
  dcc.Interval(interval=REFRESH_RATE, id="metadata-refresh"),
  html.Div(id="metadata-container", className="metadata-container")
], className="web-app")

@callback(
  Output("metadata-container", "children"),
  Input("metadata-refresh", "n_intervals")
)
def update_metadata(n_intervals):
  global incoming_packet
  if ser.in_waiting > 0:
    incoming_packet = ser.readline().decode()[0:-2].split("\t")
    print(incoming_packet)
  
  if len(incoming_packet) < 6:
    incoming_packet.extend(["" for _ in range(6 - len(incoming_packet))])
  
  time_stamp, operating_mode, holddown_status, counting, timer_left, vehicle_packet_available = incoming_packet
  timer_left: str | None
  
  if timer_left == "":
    timer = "T + 00:00:00"
  elif timer_left is not None:
    if timer_left.startswith("-"):
      sign = "+"
      timer_left = int(timer_left[1:])
    else:
      sign = "-"
      timer_left = int(timer_left)
    
    secs = timer_left % 60
    mins = timer_left // 60
    hrs = mins // 60
    mins = mins % 60
    
    timer = f"T {sign} {hrs:02d}:{mins:02d}:{secs:02d}"
  
  return html.Div([
    html.H1(timer, className="timer"),
    html.Div([
      html.Div(time_stamp, className="metadata-element"),
      html.Div(operating_mode, className="metadata-element"),
      html.Div(holddown_status, className="metadata-element"),
      html.Div(counting, className="metadata-element")
    ], className="metadata-row")
  ], className="metadata-blockset")

@callback(
  Output("blank-container", "children", allow_duplicate=True),
  Input("command-0", "n_clicks"),
  prevent_initial_call = True
)
def abort(n_clicks):
  ser.write("0".encode())
  return html.H1("ABORTED! Reset to continue...")

@callback(
  Output("blank-container", "children", allow_duplicate=True),
  Input("command-1", "n_clicks"),
  prevent_initial_call = True
)
def idle(n_clicks):
  ser.write("1".encode())

@callback(
  Output("blank-container", "children", allow_duplicate=True),
  Input("command-2", "n_clicks"),
  prevent_initial_call = True
)
def countdown(n_clicks):
  ser.write("2".encode())

@callback(
  Output("blank-container", "children", allow_duplicate=True),
  Input("command-3", "n_clicks"),
  prevent_initial_call = True
)
def freeze(n_clicks):
  ser.write("3".encode())

@callback(
  Output("blank-container", "children", allow_duplicate=True),
  Input("command-4", "n_clicks"),
  prevent_initial_call = True
)
def ignition_sequence_start(n_clicks):
  ser.write("4".encode())

@callback(
  Output("blank-container", "children", allow_duplicate=True),
  Input("command-5", "n_clicks"),
  prevent_initial_call = True
)
def reset(n_clicks):
  ser.write("5".encode())
  return ""

@callback(
  Output("blank-container", "children", allow_duplicate=True),
  Input("command-6", "n_clicks"),
  prevent_initial_call = True
)
def liftoff(n_clicks):
  ser.write("6".encode())

@callback(
  Output("blank-container", "children", allow_duplicate=True),
  Input("command-7", "n_clicks"),
  prevent_initial_call = True
)
def lost_comms(n_clicks):
  ser.write("7".encode())

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8050, debug=True)