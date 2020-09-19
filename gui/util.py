from PyQt5.QtSql import QSqlDatabase


class DBConnection:
    """Utility class.
       Provides functionality for opening and closing
       db connections for clean resource management."""
    def __init__(self):
        self._db = QSqlDatabase().addDatabase("QSQLITE")
        self._db.setDatabaseName("records.db")

    def open_db(self):
        if not self._db.isOpen():
            self._db.open()
        else:
            print("Feck off, the db is already open")

    def close_db(self):
        if self._db.isOpen():
            self._db.close()
        else:
            print("Feck off, the db is already closed")

    def db(self):
        return self._db