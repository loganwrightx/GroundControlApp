#enum OperatingMode : uint8_t {
#  OM_ABORT = 0,
#  OM_IDLE,
#  OM_COUNTING_DOWN,
#  OM_FREEZE,
#  OM_IGNITION_SEQUENCE_START,
#  OM_RESET,
#  OM_LIFTOFF,
#  OM_LOST_COMMS
#};

from enum import Enum

class OperatingMode(Enum):
  OM_ABORT = 0
  OM_IDLE = 1
  OM_COUNTING_DOWN = 2
  OM_FREEZE = 3
  OM_IGNITION_SEQUENCE_START = 4
  OM_RESET = 5
  OM_LIFTOFF = 6
  OM_LOST_COMMS = 7

operating_modes = [
  "OM_ABORT",
  "OM_IDLE",
  "OM_COUNTING_DOWN",
  "OM_FREEZE",
  "OM_IGNITION_SEQUENCE_START",
  "OM_RESET",
  "OM_LIFTOFF",
  "OM_LOST_COMMS"
]

__all__ = [
  "OperatingMode",
  "operating_modes"
]