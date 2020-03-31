from PyQt5.Qt import QApplication
from PyQt5.QtSql import QSqlDatabase


class DBConnection:
    """Utility class.
       Provides functionality for opening and closing
       db connections for clean resource management."""

    class __DBConnection:
        def __init__(self):
            self._db = QSqlDatabase().addDatabase("QSQLITE")
            self._db.setDatabaseName("records.db")

        def db(self):
            return self._db

    _instance = None

    def __init__(self):
        if DBConnection._instance is None:
            DBConnection._instance = DBConnection.__DBConnection()
        self._db = DBConnection._instance.db()
        self.db().close()
        # Creating more than one object automatically open connection
        # Explicitly close until connection is needed

    def open_db(self):
        if not self._db.isOpen():
            self._db.open()

    def close_db(self):
        if self._db.isOpen():
            self._db.close()

    def db(self):
        return self._db


class ScreenDimensions:
    def __init__(self):
        self._screen_height = QApplication.desktop().size().height()
        self._screen_width = QApplication.desktop().size().width()

    def screen_height(self):
        return self._screen_height

    def screen_width(self):
        return self._screen_width
