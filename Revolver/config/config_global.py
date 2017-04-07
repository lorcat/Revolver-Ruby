"""
Configuration file
"""
import Revolver
from Revolver.config.keys import *

# define default paths
PATH_MOTOR_FILTER = ["llab/motor/"]

# define server
DEVICE_SERVER = 'tango://haspllabcl1:10000/'
DEVICE_SERVER_P02 = 'tango://haspllabcl1:10000/'

# default motor for tests
DEVICE_MOTOR = DEVICE_SERVER + "llab/motor/mot.11"

# define retry time in case of device error
DEVICE_RETRY_INTERVAL = 5
# define flag which set if system should retry for disconnected device
DEVICE_ALLOW_RETRY = True

# macro server
SETTINGS_MACRO_SERVER = "tango://haspp02ch2:10000/p02/macroserver/haspp02ch2.01"

# door object
BL_DEFAULT_DOOR = "tango://haspp02ch2:10000/p02/door/haspp02ch2.01"


# define device human nick names to access in the program
DEVICE_NAMES = {
                'RBX': 'llab/motor/mot.11',   # +
                'RBY': 'llab/motor/mot.12',   # +
                'RBZ': 'llab/motor/mot.15',   # +
                'RBZOOM': 'llab/motor/mot.14',  # +
}

# html
HTML = {
    # filled by the application
    HTML_CALC_PATH : None,
    HTML_POS_PATH: None
}


# window size
DEFAULT_WINDOW_SIZE = (950, 410)
DEFAULT_WINDOW_POS = (200, 200)