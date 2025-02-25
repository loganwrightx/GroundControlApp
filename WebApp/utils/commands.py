from enum import Enum

class Commands(Enum):
  ABORT = 0
  BEGIN_COUNTDOWN = 1
  FREEZE = 2
  VALIDATE_VEHICLE = 3
  HOLDDOWN_ENGAGE = 4
  HOLDDOWN_DISENGAGE = 5
  RESET_COUNTDOWN = 6
  SET_COUNTDOW = 7

commands = [
  "ABORT",
  "BEGIN_COUNTDOWN",
  "FREEZE",
  "VALIDATE_VEHICLE",
  "HOLDDOWN_ENGAGE",
  "HOLDDOWN_DISENGAGE",
  "RESET_COUNTDOWN",
  "SET_COUNTDOWN"
]

__all__ = [
  "Commands",
  "commands"
]