"""The main script for the budget_tracker project.

    The program first checks if the wb_budget.xlsx workbook exists,
    if not one is created and setup. Otherwise the existing workbook
    will be opened.

    The new or existing workbook is stored in variable "wb" for later
    use.
"""







def main():
    wb = access_workbook()
    wb.save(F_NAME)












if __name__ == '__main__':
    main()
