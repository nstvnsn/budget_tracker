"""BalanceWorksheet class.
    """
from openpyxl.styles import Alignment, Color, fills, PatternFill,  Font, NamedStyle
from openpyxl.utils.cell import column_index_from_string

from .budget_worksheet import BudgetWorksheet
from workbook_init_scripts.border_presets import title_borders


class BalanceWorksheet(BudgetWorksheet):
    """A modified openpyxl worksheet class
        """
    def __init__(self, parent, title=None):
        BudgetWorksheet.__init__(self, parent, title)
        self.set_title_header()
        self.style_title_header()
        self.set_field_headers()

    # ------------------------- IncomeWorksheet Class Methods -----------------------------
    # --------------------------- Methods for sheet headers ---------------------
    def set_title_header(self):
        """
            Merges cells at top of sheet to from title area.
            Add title to merged cells.
        """
        self.merge_cells('A1:D3')
        self.cell(row=1, column=1, value='Balance')

    def style_title_header(self):
        """
        Creates a NamedStyle object and applies the style
        to the sheet title.

        Adds border sheet header.
        """

        title_style = NamedStyle(name='balance_title')
        title_style.font = Font(size=20, bold=True, underline='single',)
        title_style.alignment = Alignment(horizontal='center', vertical='center')
        title_style.fill = PatternFill(fgColor=Color("6666CC"), fill_type=fills.FILL_SOLID)
        c = self.cell(row=1, column=1)
        c.style = title_style

        title_borders(self, 'A1:D3')

    # --------------------------- Methods for sheet headers ---------------------
    def set_field_headers(self):
        """
        Sets the name and column widths of the field headers
        in the sheet.

        -Expense
        -Income
        -Balance
        """

        # Field header ranges
        f_ranges = {'Expense': 'A4:B4',
                    'Income': 'C4:D4',
                    'Balance': 'B8:C8'}

        for column in ('A', 'B', 'C', 'D'):
            self.column_dimensions[column].width = 15

        for index, (key, value) in enumerate(f_ranges.items()):
            # Find first cell of field header range
            # Find column and row number of that cell
            first = value.split(':')[0]
            col = column_index_from_string(first[0])
            row = int(first[1])
            c = self.cell(row=row, column=col, value=key)
            c.alignment = Alignment(horizontal='center')

            # Merge field header cells
            self.merge_cells(value)

    def style_field_headers(self):
        """
        Styles the fields headers in the sheet.
            -font
            -border
            -alignment

        To be implemented by one of four subclasses.
        """

        print("To be implemented by one of four subclasses.")