"""The main script for the budget_tracker project.

    Entry point for the App.
"""

from gui.kconfig import set_kivy_config

from gui.main_view_kivy import BudgetTracker


def main():
    set_kivy_config()
    BudgetTracker().run()


if __name__ == '__main__':
    main()
