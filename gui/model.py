from PyQt5.QtSql import QSqlRelationalTableModel


class IncomeRecordsModel(QSqlRelationalTableModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_records_model()

    def init_records_model(self):
        self.setTable("Income")
        self.select()
        self.setEditStrategy(QSqlRelationalTableModel.OnFieldChange)


class ExpenseRecordsModel(QSqlRelationalTableModel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_records_model()

    def init_records_model(self):
        self.setTable("Expense")
        self.select()
        self.setEditStrategy(QSqlRelationalTableModel.OnFieldChange)
