from PyQt5.QtSql import QSqlRelationalTableModel


class IncomeRecordsModel(QSqlRelationalTableModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initRecordsModel()

    def initRecordsModel(self):
        self.setTable("Income")
        self.select()
        self.setEditStrategy(QSqlRelationalTableModel.OnFieldChange)


class ExpenseRecordsModel(QSqlRelationalTableModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.initRecordsModel()

    def initRecordsModel(self):
        self.setTable("Expense")
        self.select()
        self.setEditStrategy(QSqlRelationalTableModel.OnFieldChange)
