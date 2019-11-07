"""
ControlWorksheet class
Inherits BudgetWorksheet class
"""

from .budget_worksheet import BudgetWorksheet
from workbook_init_scripts.named_styles import title_style_c


class ControlWorksheet(BudgetWorksheet):
    """Inherits from openpyxl.worksheet.worksheet.Worksheet

    Intended to serve as a typical .xlsx control sheet.
    Currently void of any control values.
    """
    def __init__(self, parent, title=None):
        BudgetWorksheet.__init__(self, parent, title)
        self.set_title_header()

    # ------------------------- ControlWorksheet Class Methods -----------------------------
    def set_title_header(self):
        """
        Set alignment, font, fill, and border properties
        for the title cell.

        Merge the first cell with range of cells that will
        comprise the sheet title header.
        """

        self['A1'].value = 'Control'
        self['A1'].style = title_style_c
        self.merge_cells('A1:F3')
