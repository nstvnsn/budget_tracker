"""
    Deprecated, saved as a reminder of which functions are left
    to migrate into classes as methods
"""

from openpyxl import Workbook
from . import sheet_style as swb


def create(wb):

    # Add and style titles for each sheet
    swb.style_titles(wb)

    # Add and style titles for each field in each worksheet
    swb.align_field_headers(wb)
    swb.set_balance_fv_placeholders(wb['Balance'])
    swb.add_field_header_borders(wb)

    wb.save('./wb_budget.xlsx')

    return wb
