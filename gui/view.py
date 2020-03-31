import calendar

from PyQt5.Qt import Qt
from PyQt5.QtWidgets import (QComboBox, QFrame, QHBoxLayout, QHeaderView,
                             QLabel, QMainWindow, QPushButton, QRadioButton,
                             QSpacerItem, QTableView, QVBoxLayout, QWidget)

from .model import ExpenseRecordsModel, IncomeRecordsModel
from .util import DBConnection, ScreenDimensions


class RecordsView(QTableView):
    def __init__(self, parent, *args, r_type='income', **kwargs):
        super().__init__(parent)
        self._header = self.horizontalHeader()
        self._model = IncomeRecordsModel()  # The current model used
        self.init_records_view()

    def init_records_view(self):

        screen_w, screen_h = ScreenDimensions().screen_width(), ScreenDimensions().screen_height()
        min_height = screen_h * 0.3
        max_height = screen_h * 0.7

        self.setFrameStyle(QFrame.Box)
        self.setLineWidth(0)
        self.setMinimumHeight(min_height)
        self.setMaximumHeight(max_height)
        self.setModel(self._model)
        self.setColumnHidden(0, True)
        self.setColumnHidden(1, True)
        self._header.setMinimumSectionSize(screen_w // 5)

    def resizeEvent(self, event) -> None:
        super(QTableView, self).resizeEvent(event)
        self._header.setSectionResizeMode(QHeaderView.Stretch)

        for column in range(self._header.count()):
            width = self._header.sectionSize(column)
            self._header.setSectionResizeMode(column, QHeaderView.Interactive)
            self._header.resizeSection(column, width)

        self._header.setCascadingSectionResizes(True)


class DisplayButtonsBar(QFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Display Buttons Bar widgets list
        self._dp_bar_frames = []

        # Record type selector frame and push buttons
        self._rec_type_frame = QFrame()
        self._rec_type_buttons = {"income": QPushButton(),
                                  "expense": QPushButton()}
        self._dp_bar_frames.append(self._rec_type_frame)

        # Range type selector frame and radio buttons
        self._range_type_frame = QFrame()
        self._range_type_buttons = {"last": QRadioButton(),
                                    "from": QRadioButton()}

        # Last X Days frame, combo box, and label
        self._last_frame = QFrame()
        self._days_combo = QComboBox()
        self._days_label = QLabel()

        # From day x to day y frame, combo boxes and label
        self._from_frame = QFrame()
        self._from_combo_boxes = {"day": QComboBox(),
                                  "month": QComboBox(),
                                  "year": QComboBox()}
        self._to_label = QLabel()
        self._to_combo_boxes = {"day": QComboBox(),
                                "month": QComboBox(),
                                "year": QComboBox()}

        # Vertical frame for Last X Days frame and From X to Y frame
        self._last_from_combo_frame = QFrame()

        # Horizontal frame combining the radio buttons frame and range combo box frame
        self._type_and_range_frame = QFrame()
        self._dp_bar_frames.append(self._type_and_range_frame)

        # Show push button frame and button
        self._show_frame = QFrame()
        self._show_button = QPushButton()
        self._dp_bar_frames.append(self._show_frame)

        self._init_display_buttons()
        self.init_display_buttons_bar()

    def _init_display_buttons(self):
        height = ScreenDimensions().screen_height() * 0.25
        btn_size = {"h": int(height * 0.10),
                    "w": int(height * 0.35)}
        lbl_size = {"h": int(height * 0.3),
                    "w": int(height * 0.35)}

        for key, button in self._rec_type_buttons.items():  # Income and Expense buttons
            button.setFixedHeight(btn_size["h"])
            button.setFixedWidth(btn_size["w"])
            button.setText(key[0].upper() + key[1:])

        self._show_button.setText("Show")
        self._show_button.setFixedHeight(btn_size["h"] * 3)
        self._show_button.setFixedWidth(btn_size["w"])

        for key, button in self._range_type_buttons.items():  # Last and From radio buttons
            button.setFixedHeight(lbl_size["h"])
            button.setFixedWidth(lbl_size["w"])
            button.setText(key[0].upper() + key[1:])

        self._days_combo.setFixedHeight(btn_size["h"])
        self._days_combo.setFixedWidth(btn_size["w"])
        self._days_combo.addItems([f"{x}" for x in [30, 60, 90]])
        self._days_label.setText("Days")
        self._days_label.setFixedHeight(lbl_size["h"])

        days = [f"{x}" for x in range(1, 31)]
        months = ["Jan", "Feb", "March",
                  "April", "May", "June",
                  "July", "August", "September",
                  "October", "November", "December"
                  ]
        # TODO Change range from 30 years before current year to current year
        years = [f"{x}" for x in range(1980, 2050)]
        for cmb in self._from_combo_boxes.values():
            cmb.setFixedHeight(btn_size["h"])
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
        height = ScreenDimensions().screen_height() * 0.25
        display_buttons_bar_layout = QHBoxLayout()
        margin = int(height * 0.1)
        type_t_margin = int(height * 0.02)
        type_b_margin = int(height * 0.032)
        type_l_margin = int(height * 0.049)
        range_r_margin = int(height * 0.049)
        separator_line = int(height * 0.005)

        rec_type_layout = QHBoxLayout()
        rec_type_layout.addWidget(self._rec_type_buttons["income"])
        rec_type_layout.addWidget(self._rec_type_buttons["expense"])
        rec_type_layout.setAlignment(Qt.AlignTop)
        self.setFixedHeight(height)
        self.setFrameStyle(QFrame.Box)
        self._rec_type_frame.setLayout(rec_type_layout)
        self.setLineWidth(0)

        show_layout = QVBoxLayout()
        show_layout.addWidget(self._show_button)
        show_layout.setAlignment(Qt.AlignCenter)
        self._show_frame.setLayout(show_layout)

        range_type_layout = QVBoxLayout()
        range_type_layout.addWidget(self._range_type_buttons["last"])
        range_type_layout.addStretch(1)
        range_type_layout.addWidget(self._range_type_buttons["from"])
        range_type_layout.setAlignment(Qt.AlignCenter)
        self._range_type_frame.setAutoFillBackground(True)
        range_type_layout.setContentsMargins(type_l_margin, type_t_margin, 0, type_b_margin)
        self._range_type_frame.setFrameStyle(QFrame.Box)
        self._range_type_frame.setLineWidth(0)
        self._range_type_frame.setLayout(range_type_layout)
        self._range_type_frame.setObjectName("range_type")
        self._range_type_frame.setStyleSheet("""QFrame#range_type {
                                                    background: rgba(0, 0, 0, 0);
                                                    }""")

        last_layout = QHBoxLayout()
        last_layout.addWidget(self._days_combo)
        last_layout.addWidget(self._days_label)
        last_layout.setContentsMargins(0, 0, 0, 0)
        self._last_frame.setFrameStyle(QFrame.Box)
        self._last_frame.setLayout(last_layout)
        self._last_frame.setLineWidth(0)

        from_layout = QHBoxLayout()
        for key in sorted(self._from_combo_boxes.keys()):
            from_layout.addWidget(self._from_combo_boxes[key])
        from_layout.addWidget(self._to_label)  # Adds "To" label between sets of combo boxes
        for key in sorted(self._to_combo_boxes.keys()):
            from_layout.addWidget(self._to_combo_boxes[key])
        from_layout.setContentsMargins(0, 0, 0, 0)
        self._from_frame.setLayout(from_layout)

        line = QFrame()  # For setting the Hline used to separate the range date selectors
        line.setFrameStyle(QFrame.HLine)
        line.setFixedHeight(separator_line)
        line.setStyleSheet("border: None; \
                            background: rgb(100, 100, 100);")

        last_from_combo_layout = QVBoxLayout()
        last_from_combo_layout.addWidget(self._last_frame)
        last_from_combo_layout.addWidget(line)
        last_from_combo_layout.addWidget(self._from_frame)
        self._last_from_combo_frame.setAutoFillBackground(True)
        last_from_combo_layout.setContentsMargins(0, 0, range_r_margin, 0)
        self._last_from_combo_frame.setFrameStyle(QFrame.Box)
        self._last_from_combo_frame.setLayout(last_from_combo_layout)
        self._last_from_combo_frame.setLineWidth(0)
        self._last_from_combo_frame.setObjectName("last_from")
        self._last_from_combo_frame.setStyleSheet("""QFrame#last_from {
                                                        background: rgba(0, 0, 0, 0)}""")

        type_and_range_layout = QHBoxLayout()
        type_and_range_layout.addWidget(self._range_type_frame)
        type_and_range_layout.addWidget(self._last_from_combo_frame)
        type_and_range_layout.setSpacing(0)
        self._type_and_range_frame.setLayout(type_and_range_layout)
        self._type_and_range_frame.setObjectName("type_and_range")
        self._type_and_range_frame.setStyleSheet("""QFrame#type_and_range {
                                                        background: rgba(60, 100, 120, 100);
                                                        border-radius: 10%
                                                        }""")

        for frame in self._dp_bar_frames:
            display_buttons_bar_layout.addWidget(frame)
        display_buttons_bar_layout.insertStretch(1, 1)
        display_buttons_bar_layout.setAlignment(Qt.AlignCenter)
        display_buttons_bar_layout.setContentsMargins(0, margin, 0, margin)
        display_buttons_bar_layout.setSpacing(0)

        self.setLayout(display_buttons_bar_layout)
        self.setObjectName("display_buttons_bar")
        self.setStyleSheet("""QFrame#display_buttons_bar {
                                        background: rgba(120, 145, 170, 255)}""")


class CentralFrame(QFrame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self._display_buttons_bar = DisplayButtonsBar(self)
        self._records_view = RecordsView(self)

        self._init_central_layout()

    def _init_central_layout(self) -> None:
        layout = QVBoxLayout()
        layout.addWidget(self._records_view)
        layout.addWidget(self._display_buttons_bar)
        layout.setAlignment(Qt.AlignTop)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        self.setObjectName("central_frame")
        self.setLayout(layout)

    # Accessor Methods
    def records_view(self) -> RecordsView:
        return self._records_view

    def display_buttons_bar(self) -> DisplayButtonsBar:
        return self._display_buttons_bar


class Main(QMainWindow):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._db = DBConnection()
        self._central_widget = CentralFrame(self)
        self.init_main()

    def init_main(self) -> None:
        win_height = ScreenDimensions().screen_height()
        win_width = ScreenDimensions().screen_width()
        self.setMinimumSize(win_width // 2.5, win_height // 1.5)
        #self.resize(win_width, win_height)
        self.setGeometry(0, 0, win_width, win_height)
        self.setCentralWidget(self._central_widget)
        self.show()
