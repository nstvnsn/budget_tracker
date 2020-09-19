import calendar

from PyQt5.Qt import Qt
from PyQt5.QtWidgets import (QComboBox, QFrame, QHBoxLayout,
                             QLabel, QMainWindow, QPushButton, QRadioButton,
                             QSpacerItem, QTableView, QVBoxLayout, QWidget)

from .model import ExpenseRecordsModel, IncomeRecordsModel
from .util import DBConnection


class RecordsView(QFrame):
    def __init__(self, parent, *args, r_type='income', **kwargs):
        super().__init__(parent)
        self._db = DBConnection()
        print(self._db.db().isOpen())
        self._wh = parent.frameGeometry().height()
        self._layout = QVBoxLayout()
        self._model = IncomeRecordsModel()  # The current model used
        self._records_box = QTableView()
        self.init_records_view()

    def init_records_view(self):
        self.setFrameStyle(QFrame.Box)
        self.setLineWidth(2)
        self.setMaximumHeight(self._wh * 0.6)
        self._records_box.setModel(self._model)
        self._records_box.setColumnHidden(0, True)
        self._records_box.setColumnHidden(1, True)
        self._layout.addWidget(self._records_box)
        self.setLayout(self._layout)


class DisplayButtonsBar(QFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__()
        self._wh = parent.frameGeometry().height()
        self._btn_size = {"h": int(self._wh * 0.05),
                          "w": int(self._wh * 0.15)}
        self._lbl_size = {"h": int(self._wh * 0.08),
                          "w": int(self._wh * 0.15)}

        self._display_buttons_bar_layout = QHBoxLayout()
        self._dp_bar_widgets = []

        self._rec_type_layout = QHBoxLayout()
        self._rec_type_widget = QFrame()
        self._rec_type_buttons = {"income": QPushButton(),
                                  "expense": QPushButton()}
        self._dp_bar_widgets.append(self._rec_type_widget)


        self._show_layout = QVBoxLayout()
        self._show_widget = QFrame()
        self._show_button = QPushButton()
        self._dp_bar_widgets.append(self._show_widget)

        self._range_type_layout = QVBoxLayout()
        self._range_type_widget = QFrame()
        self._range_type_buttons = {"last": QRadioButton(),
                                    "from": QRadioButton()}
        self._dp_bar_widgets.append(self._range_type_widget)

        self._last_layout = QHBoxLayout()
        self._last_widget = QFrame()
        self._days_combo = QComboBox()
        self._days_label = QLabel()

        self._from_layout = QHBoxLayout()
        self._from_widget = QFrame()
        self._from_combo_boxes = {"day": QComboBox(),
                                  "month": QComboBox(),
                                  "year": QComboBox()}
        self._to_label = QLabel()
        self._to_combo_boxes = {"day": QComboBox(),
                                "month": QComboBox(),
                                "year": QComboBox()}

        self._last_from_combo_layout = QVBoxLayout()
        self._last_from_combo_widget = QFrame()
        self._dp_bar_widgets.append(self._last_from_combo_widget)

        self._init_display_buttons()
        self.init_display_buttons_bar()

    def _init_display_buttons(self):
        for key, button in self._rec_type_buttons.items():  # Income and Expense buttons
            button.setFixedHeight(self._btn_size["h"])
            button.setFixedWidth(self._btn_size["w"])
            button.setText(key[0].upper() + key[1:])

        self._show_button.setText("Show")
        self._show_button.setFixedHeight(self._btn_size["h"])
        self._show_button.setFixedWidth(self._btn_size["w"])

        for key, button in self._range_type_buttons.items():  # Last and From radio buttons
            button.setFixedHeight(self._lbl_size["h"])
            button.setFixedWidth(self._lbl_size["w"])
            button.setText(key[0].upper() + key[1:])

        self._days_combo.setFixedHeight(self._btn_size["h"])
        self._days_combo.setFixedWidth(self._btn_size["w"])
        self._days_combo.addItems([f"{x}" for x in [30, 60, 90]])
        self._days_label.setText("Days")
        self._days_label.setFixedHeight(self._lbl_size["h"])

        days = [f"{x}" for x in range(1, 31)]
        months = ["Jan", "Feb", "March",
                  "April", "May", "June",
                  "July", "August", "September",
                  "October", "November", "December"
                  ]
        years = [f"{x}" for x in range(1980, 2050)]
        for cmb in self._from_combo_boxes.values():
            cmb.setFixedHeight(self._btn_size["h"])
        self._from_combo_boxes["day"].addItem("DD")
        self._from_combo_boxes["day"].addItems(days)
        self._from_combo_boxes["month"].addItem("MM")
        self._from_combo_boxes["month"].addItems(months)
        self._from_combo_boxes["year"].addItem("YYYY")
        self._from_combo_boxes["year"].addItems(years)
        self._to_label.setText("To")
        self._to_combo_boxes["day"].addItem("DD")
        self._to_combo_boxes["day"].addItems(days)
        self._to_combo_boxes["month"].addItem("MM")
        self._to_combo_boxes["month"].addItems(months)
        self._to_combo_boxes["year"].addItem("YYYY")
        self._to_combo_boxes["year"].addItems(years)

    def init_display_buttons_bar(self):
        self.setFrameStyle(QFrame.Box)
        self.setLineWidth(2)
        self.setMaximumHeight(self._wh * 0.25)
        self._rec_type_layout.addWidget(self._rec_type_buttons["income"])
        self._rec_type_layout.addWidget(self._rec_type_buttons["expense"])
        self._rec_type_layout.setAlignment(Qt.AlignTop)
        self._rec_type_layout.setContentsMargins(0, 0, 0, 0)
        self._rec_type_widget.setLayout(self._rec_type_layout)

        self._show_layout.setAlignment(Qt.AlignTop)
        self._show_layout.setContentsMargins(0, self._wh * 0.035, 0, 0)
        self._show_layout.addWidget(self._show_button)
        self._show_widget.setLayout(self._show_layout)

        self._range_type_layout.addWidget(self._range_type_buttons["last"])
        self._range_type_layout.addStretch(1)
        self._range_type_layout.addWidget(self._range_type_buttons["from"])
        self._range_type_widget.setLayout(self._range_type_layout)

        self._last_layout.setContentsMargins(0, 0, 0, 0)
        self._last_layout.addWidget(self._days_combo)
        self._last_layout.addWidget(self._days_label)
        self._last_widget.setLayout(self._last_layout)
        self._last_widget.setFrameStyle(QFrame.Box)
        self._last_widget.setLineWidth(2)


        for key in sorted(self._from_combo_boxes.keys()):
            self._from_layout.addWidget(self._from_combo_boxes[key])
        self._from_layout.addWidget(self._to_label)  # Adds "To" label between sets of combo boxes
        self._from_layout.setContentsMargins(0, 0, 0, 0)
        for key in sorted(self._to_combo_boxes.keys()):
            self._from_layout.addWidget(self._to_combo_boxes[key])
        self._from_widget.setLayout(self._from_layout)

        self._last_from_combo_layout.setContentsMargins(0, 0, 0, 0)
        self._last_from_combo_layout.addWidget(self._last_widget)
        self._last_from_combo_layout.addWidget(self._from_widget)
        self._last_from_combo_widget.setLayout(self._last_from_combo_layout)
        self._last_from_combo_widget.setFrameStyle(QFrame.Box)
        self._last_from_combo_widget.setLineWidth(2)

        self._display_buttons_bar_layout.setAlignment(Qt.AlignCenter)
        self._display_buttons_bar_layout.setContentsMargins(0, 0, 0, 0)
        self._display_buttons_bar_layout.setSpacing(0)
        for widget in self._dp_bar_widgets:
            self._display_buttons_bar_layout.addWidget(widget)
        self._display_buttons_bar_layout.insertStretch(1, 1)
        self.setLayout(self._display_buttons_bar_layout)


class CentralLayout(QVBoxLayout):
    def __init__(self, parent):
        super().__init__(parent)
        self._records_view = RecordsView(parent)
        self._display_buttons_bar = DisplayButtonsBar(parent)
        self.init_central_layout()

    def init_central_layout(self):
        self.setAlignment(Qt.AlignTop)
        self.addWidget(self._records_view)
        self.addSpacing(10)
        self.addWidget(self._display_buttons_bar)


class Main(QMainWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.win_x = 1920
        self.win_y = 1080
        self._central_layout = CentralLayout(self)  # Central Layout
        self._central_widget = QWidget()  # Central Widget
        self.init_main()

    def init_main(self):
        self.setMinimumSize(self.win_x // 2, self.win_y // 2)
        self._central_widget.setLayout(self._central_layout)  # Central layout applied to central widget
        self.setCentralWidget(self._central_widget)
        self.show()
