from PyQt5.QtSql import QSqlDatabase


class DBConnection():
    """Utility class.
       Provides functionality for opening and closing
       db connections for clean resource management."""

    def open_db(self):
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("records.db")

    def close_db(self):
        self.db.close()
