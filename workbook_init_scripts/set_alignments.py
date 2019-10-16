def align_range(ws, cell_range, alignment=None):

    for row in ws[cell_range]:
        for c in row:
            c.alignment = alignment
