from screeninfo import get_monitors, Monitor

import kivy
from kivy.app import App
from kivy.core.window import WindowBase, Window
from kivy.graphics import Color, Rectangle
from kivy.uix.gridlayout import GridLayout
from kivy.uix.recyclegridlayout import RecycleGridLayout
from kivy.uix.recycleview import RecycleView
from kivy.uix.label import Label
from kivy.uix.widget import Widget


kivy.require("1.11.1")


class RecordsRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super(RecordsRecycleView, self).__init__(**kwargs)
        self.data = [{"text": x} for x in range(100)]


class MainWindowGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class BudgetTracker(App):

    def build(self):
        main_window = MainWindowGrid()
        return main_window


if __name__ == "__main__":
    BudgetTracker().run()
