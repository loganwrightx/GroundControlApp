import serial
import glob

if __name__ == "__main__":
  ser = serial.Serial(port="/dev/tty.usbmodem101", baudrate=115200)
  
  while True:
    if ser.in_waiting > 0:
      data = ser.readline().decode()[0:-2].split("\t")
      print(data)
  
  #print(glob.glob("/dev/tty.*"))