"""The main script for the budget_tracker project.



    The new or existing workbook is stored in variable "wb" for later
    use.
"""
from kivy import Config  # Move this block to main.py eventually
# Config.set('graphics', 'width', '2000')
# Config.set('graphics', 'height', '1200')
# Config.set('graphics', 'minimum_width', '800')
# Config.set('graphics', 'minimum_height', '900')
# Config.set('graphics', 'position', 'auto')

import gui.kconfig

from gui.main_view_kivy import BudgetTracker


def main():

    BudgetTracker().run()


if __name__ == '__main__':
    main()
