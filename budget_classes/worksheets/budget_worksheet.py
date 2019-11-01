"""BudgetWorksheet class, inheriting from openpyxl.worksheet.worksheet"""
from openpyxl.worksheet.worksheet import Worksheet


class BudgetWorksheet(Worksheet):
    """BudgetWorksheet inherits from openpyxl.worksheet.worksheet.Worksheet
        To be further inherited by a more specific worksheet subclass.
        Typically one of the following four:
            -ExpensesWorksheet
            -IncomeWorksheet
            -BalanceWorksheet
            -ControlsWorksheet
    """

    # ----------------------- Overridden Class Methods -----------------------------
    def __init__(self, parent, title=None):
        Worksheet.__init__(self, parent, title)

# ------------------------- BudgetWorksheet Class Methods -----------------------------
# --------------------------- Methods for sheet headers ---------------------
    def set_title_header(self):
        """
            Merges cells at top of sheet to from title area.
        """

        print("To be implemented by one of four subclasses.")

    def style_title_header(self):
        """
        Creates a NamedStyle object and applies the style
        to the sheet title.

        Adds border sheet header.
        """

        print("To be implemented by one of four subclasses.")

    # --------------------------- Methods for sheet headers ---------------------
    def set_field_labels(self):
        """
        Sets the name and column widths of the field headers
        in the sheet.

        To be implemented by one of four subclasses.
        """

        print("To be implemented by one of four subclasses.")

    def style_field_labels(self):
        """
        Styles the fields headers in the sheet.
            -font
            -border
            -alignment

        To be implemented by one of four subclasses.
        """

        print("To be implemented by one of four subclasses.")