"""
NOT IN USE AT THE MOMENT
ExpenseRecord class
For adding expense records to the expense worksheet.
"""


class ExpenseRecord:
    def __init__(self, date=None, expense=None, cost=None):
        self._date = date
        self._expense = expense
        self._cost = cost

    # Accessors
    def date(self):
        return self._date

    def expense(self):
        return self._expense

    def cost(self):
        return self._cost

    # Mutators
    def set_date(self, date):
        self._date = date

    def set_expense(self, expense):
        self._expense = expense

    def set_cost(self, cost):
        try:
            cost = float(cost)
            if cost >= 0:
                self._cost = cost
        except TypeError:
            print("The expense cost must be of numerical value >= 0.")

    # Interactions with ExpenseWorksheet
    """
    Have not been able to modify openpyxl.load_workbook to use
    my derived worksheet classes. Until I do, they serve only as 
    a template builder and no new methods will be accessible when
    these sheets are loaded. Essentially, the load_workbook loads
    them as an original Worksheet class object.
    """

    def add_new_record(self, expense_ws):
        if expense_ws['A5'] is not None:
            expense_ws.insert_rows(idx=5)

        expense_ws['A5'].value = self.date()
        expense_ws['B5'].value = self.expense()
        expense_ws['C5'].value = self.cost()
        expense_ws['C5'].number_format = '$#,##0.00'

    def remove_record(self, expense_ws, row_num):
        """
        Removes record located in the worksheet at a given row.
        Returns record object.

        :param expense_ws:
        :param row_num:
        :return:
        """
        if expense_ws['A'+str(row_num)] is None:
            """
            No record at given row, print message stating so.
            """
            print("No record exists")
            return

        _date = expense_ws['A'+row_num]
        _expense = expense_ws['B'+row_num]
        _cost = expense_ws['c'+row_num]

        self.set_date(_date)
        self.set_expense(_expense)
        self.set_cost(_cost)

        expense_ws.delete_rows(row_num, 1)
        return self
