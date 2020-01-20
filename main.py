import sys

from PyQt5.QtWidgets import QApplication

from gui.view import Main


if __name__ == "__main__":
    app = QApplication([])
    budget_tracker = Main()
    sys.exit(app.exec_())
