"""
    Searches for the existence of the program's designated workbook and,
    if none exists, creates one to be used with the main application.


    Creates the following worksheets:
        -Expenses
        -Income
        -Balance
        -Controls
        """

from openpyxl import Workbook
from . import sheet_style as swb
from . import sheet_templates as cws


def new_wb():
    """
        Create a Workbook class object and 3 additional
        sheets, and return the object.
        """
    # Creates workbook and the 4 sheets
    wb = Workbook()
    ws = wb.active
    ws.title = 'Expenses'
    wb.create_sheet('Income')
    wb.create_sheet('Balance')
    wb.create_sheet('Controls')

    return wb


def create():
    wb = new_wb()

    # Add and style titles for each sheet
    cws.set_sheet_headers(wb)
    swb.style_titles(wb)

    # Add and style titles for each field in each worksheet
    cws.set_field_headers(wb)
    swb.align_field_headers(wb)

    swb.set_balance_fv_placeholders(wb['Balance'])
    swb.add_field_header_borders(wb)

    wb.save('./wb_budget.xlsx')

    return wb
