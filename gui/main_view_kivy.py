"""
Budget Tracker with Kivy GUI
Unsure of how much behavior and logic will end up in here.
Thus far, all of the UI is implemented in budgettracker.kv
"""

import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.recycleview import RecycleView

kivy.require("1.11.1")


class RecordsRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super(RecordsRecycleView, self).__init__(**kwargs)
        self.data = [{"text": x} for x in range(100)]


class MainWindowGrid(GridLayout):
    """Implementation managed by budgettracker.kv"""
    pass


class BudgetTracker(App):

    def build(self):
        main_window = MainWindowGrid()
        return main_window


if __name__ == "__main__":
    BudgetTracker().run()
