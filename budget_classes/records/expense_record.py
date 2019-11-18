"""
ExpenseRecord class
For adding expense records to the expense worksheet.
"""


class ExpenseRecord:
    def __init__(self, date, expense, cost):
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


