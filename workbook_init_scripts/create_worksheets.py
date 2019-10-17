"""
    For each of the 4 sheets:
        -Creates sheet header
        -Creates appropriate fields for each sheet
    """


# --------------------------- Sheet Headers ---------------------------
def set_sheet_headers(wb):
    """
        Merges cells at top of each sheet to from title area.

        :param wb: excel workbook instance
        """

    worksheets = wb.worksheets

    for index, sheet in enumerate(worksheets):

        # Merges the correct cells on each sheet
        if sheet not in (wb['Balance'], wb['Controls']):
            sheet.merge_cells('A1:C3')
        elif sheet == wb['Balance']:
            sheet.merge_cells('A1:D3')
        else:
            sheet.merge_cells('A1:F3')

        hp = ('Expenses', 'Income', 'Balance', 'Controls')
        sheet.cell(row=1, column=1, value=hp[index])



