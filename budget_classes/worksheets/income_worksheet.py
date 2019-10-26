"""IncomeWorksheet class.
    """

from .budget_worksheet import BudgetWorksheet


class IncomeWorksheet(BudgetWorksheet):
    """Inherits BudgetWorksheet, a subclass
        of openpyxl.worksheet.worksheet.Worksheet class.
        """
    def __init__(self, parent, title=None):
        BudgetWorksheet.__init__(parent, title)

    # ------------------------- IncomeWorksheet Class Methods -----------------------------
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

    def set_field_headers(self):
        """
        Sets the name and column widths of the field headers
        in the sheet.

        To be implemented by one of four subclasses.
        """

        print("To be implemented by one of four subclasses.")

    def style_field_headers(self):
        """
        Styles the fields headers in the sheet.
            -font
            -border
            -alignment

        To be implemented by one of four subclasses.
        """

        print("To be implemented by one of four subclasses.")