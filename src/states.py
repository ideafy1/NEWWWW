from enum import Enum

class UserState(Enum):
    WAITING_FOR_ORIGINAL = 1
    WAITING_FOR_REPLACEMENT = 2

user_states = {}