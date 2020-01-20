from PyQt5.QtWidgets import (QFrame, QMainWindow, QTableView,
                             QVBoxLayout, QWidget)

from .model import ExpenseRecordsModel, IncomeRecordsModel
from .util import DBConnection


class RecordsView(QFrame, DBConnection):
    def __init__(self, root, *args, r_type='income', **kwargs):
        super().__init__(root, *args, **kwargs)
        self.root = root

        if r_type.upper() == 'INCOME':
            self.initIncRecordsView(root)
        elif r_type.upper() == 'EXPENSE':
            self.initExpRecordsView(root)
        else:
            raise ValueError("r_type must be 'income' or 'expense")

    def records_view_decorator(initRecordsFunc):
        def decorated(self, *args, **kwargs):
            _win_height = self.root.frameGeometry().height()

            self.setFrameStyle(QFrame.Box)
            self.setLineWidth(2)
            self.setMaximumHeight(_win_height * 0.8)

            self.open_db()  # Open db connection to use model

            records_box = QTableView()
            model = initRecordsFunc(self, *args, **kwargs)
            records_box.setModel(model)
            records_box.setColumnHidden(0, True)
            records_box.setColumnHidden(1, True)
            layout = QVBoxLayout()
            layout.addWidget(records_box)
            self.setLayout(layout)
        return decorated

    @records_view_decorator
    def initIncRecordsView(self, root):
        return IncomeRecordsModel()

    @records_view_decorator
    def initExpRecordsView(self, root):
        return ExpenseRecordsModel()


class CentralLayout(QVBoxLayout):
    def __init__(self, root):
        super().__init__(root)
        self.initRootLayout(root)

    def initRootLayout(self, root):
        # _win_width = root.frameGeometry().width()
        _win_height = root.frameGeometry().height()

        _tbl_header = QFrame()
        _tbl_header.setFrameStyle(QFrame.Box)
        _tbl_header.setLineWidth(2)
        _tbl_header.setFixedHeight(50)

        _rec_tbl_sel_btns = QFrame()
        _rec_tbl_sel_btns.setFrameStyle(QFrame.Box)
        _rec_tbl_sel_btns.setLineWidth(2)
        _rec_tbl_sel_btns.setFixedHeight(100)

        _stretch_holder = QFrame()
        _stretch_holder.setFrameStyle(QFrame.Box)
        _stretch_holder.setLineWidth(2)

        _btns_and_details = QFrame()
        _btns_and_details.setFrameStyle(QFrame.Box)
        _btns_and_details.setLineWidth(2)
        _btns_and_details.setFixedHeight(_win_height * 0.4)

        self.addWidget(_tbl_header)
        self.addWidget(RecordsView(root))
        self.addWidget(_rec_tbl_sel_btns)
        self.addWidget(_stretch_holder)
        self.addWidget(_btns_and_details)

        self.setStretch(1, 2)
        self.setStretch(4, 1)


class Main(QMainWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.initMain()

    def initMain(self):
        self.win_x = 2000
        self.win_y = 2000
        self.setMinimumSize(self.win_x, self.win_y * 0.5)

        self._window = QWidget()
        self._window.setLayout(CentralLayout(self))
        self.setCentralWidget(self._window)
        self.show()
