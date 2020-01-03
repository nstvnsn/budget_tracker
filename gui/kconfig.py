"""Configuration setup for kivy GUI

   To be executed before BudgetTracker().run() to prevent
   conflicts. To be executed before ALL other kivy imports.
"""

from os import name
from platform import system

from kivy import Config
from screeninfo import get_monitors

"""
Intend to perform check OS before configuring
in the event I decide to port this to Android.
TBD...
"""


def set_kivy_config():

    monitor = get_monitors()[0]

    window_height = str(int(monitor.height * 0.8))
    window_width = str(int(monitor.width * 0.8))
    Config.set('graphics', 'width', window_width)
    Config.set('graphics', 'height', window_height)
    Config.set('graphics', 'minimum_width', '800')
    Config.set('graphics', 'minimum_height', '900')
    Config.set('graphics', 'position', 'auto')