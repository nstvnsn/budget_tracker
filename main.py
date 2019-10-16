"""This is the main script for the budget_tracker_excel project.

    budget_tracker_excel directory:
    -workbook_init_scripts/
        -__init__.py
        -create_workbook.py
        -set_alignments.py
        -set_borders.py
        -set_cell_format.py
        -style_workbook.py
    -main.py
    -wb_budget.xlsx

    The program first checks if the wb_budget.xlsx workbook exists,
    if not one is created and setup. Otherwise the existing workbook
    will be opened."""

from openpyxl import load_workbook

from workbook_init_scripts import create_workbook, style_workbook

F_NAME = './wb_budget.xlsx'


def access_workbook():

    try:
        wb = load_workbook(F_NAME)
        print(f'Workbook "{F_NAME[2:]}" loaded')
        return wb

    except FileNotFoundError:
        print('No workbook found in program directory', end='\n\n')
        print(f'Creating new workbook "{F_NAME[2:]}"')
        wb = create_workbook.create()
        return wb

    return book


def main():
    wb = access_workbook()
    ws = wb.active


if __name__ == '__main__':
    main()
