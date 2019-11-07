"""
BudgetWorksheet class
Inherits from openpyxl.worksheet.worksheet.Worksheet
"""
from openpyxl.worksheet.worksheet import Worksheet


class BudgetWorksheet(Worksheet):
    """To be further inherited by a more specific worksheet subclass.
        Typically one of the following four:
            -ExpensesWorksheet
            -IncomeWorksheet
            -BalanceWorksheet
            -ControlsWorksheet
    """

    # ----------------------- Overridden Parent Class Methods -----------------------------
    def __init__(self, parent, title=None):
        Worksheet.__init__(self, parent, title)

# ------------------------- BudgetWorksheet Class Methods -----------------------------
    def set_title_header(self):
        """
            Merges cells at top of sheet to from title area.
        """

        print("To be implemented by one of four subclasses.")

    def set_field_labels(self):
        """
        Sets the name and column widths of the field headers
        in the sheet.

        To be implemented by one of four subclasses.
        """

        print("To be implemented by one of four subclasses.")

