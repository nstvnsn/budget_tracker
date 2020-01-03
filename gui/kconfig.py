"""Configuration setup for kivy GUI

   To run as soon as it is imported to prevent conflicts
   with other kivy modules being loaded before Config.set is run
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

monitor = get_monitors()[0]

window_height = str(int(monitor.height * 0.8))
window_width = str(int(monitor.width * 0.8))
Config.set('graphics', 'width', window_width)
Config.set('graphics', 'height', window_height)
Config.set('graphics', 'minimum_width', '800')
Config.set('graphics', 'minimum_height', '900')
Config.set('graphics', 'position', 'auto')