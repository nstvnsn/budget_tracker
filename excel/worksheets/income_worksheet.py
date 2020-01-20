"""
IncomeWorksheet class
Inherits BudgetWorksheet class
"""

from .budget_worksheet import BudgetWorksheet
from workbook_init_scripts.named_styles import label_style, title_style_i


class IncomeWorksheet(BudgetWorksheet):
    """Comprised of the following fields:
        -Date
        -Source
        -Net
    """
    def __init__(self, parent, title=None):
        BudgetWorksheet.__init__(self, parent, title)
        self.set_title_header()
        self.set_field_labels()

    # ------------------------- IncomeWorksheet Class Methods -----------------------------
    def set_title_header(self):
        """
        Set alignment, font, fill, and border properties
        for the title cell.

        Merge the first cell with range of cells that will
        comprise the sheet title header.
        """

        self['A1'].value = 'Income'
        self['A1'].style = title_style_i
        self.merge_cells('A1:C3')

    def set_field_labels(self):
        """
        Sets the alignment, border, font, and value properties
        of the cells that display the field labels.

        Sets the column width of the columns containing the fields.
        """

        # Set column widths for the 3 fields on this sheet
        self.column_dimensions['A'].width = 15
        self.column_dimensions['B'].width = 25
        self.column_dimensions['C'].width = 15

        self['A4'].value = 'Date'
        self['A4'].style = label_style

        self['B4'].value = 'Source'
        self['B4'].style = label_style

        self['C4'].value = 'Net'
        self['C4'].style = label_style

