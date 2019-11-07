"# budget_tracker_excel" 

Small Python3 project. 
Uses openpyxl to create a workbook of spreadsheets.

budget_tracker_excel directory:

    -budget_classes/
        -worksheets/
            __init__.py
            balance_worksheet.py
            budget_worksheet.py
            control_worksheet.py
            expense_worksheet.py
            income_worksheet.py
        __init__.py
        budget_workbook.py
    -workbook_init_scripts/
        -__init__.py
        -border_presets.py
        -named_styles.py
    -main.py
    -README.md
    -wb_budget.xlsx (May not exist, 
        reated when program executed 
        for the first time)

4 sheets in total:

    -Income
    -Expenses
    -Balance
    -Controls
    
    
Creates a new workbook with 4 new worksheets in root directory, unless workbook
already in existence.

Income and Expense are styled templates containing field labels that determine
the structure of the records they contain. Balance is another styled template
containing 3 separate fields instead of a collection of records. Control is
a sheet reserved for control values that are used, but is empty save for a title
header.

Expense:

    -Date
    -Purchase
    -Cost

Income:

    -Date
    -Source
    -Net
    
Balance:

    -Expense
    -Income
    -Balance

Functionality to be added:

    -Balance forecasting based on income and expenses over last 30 days
    -Form for adding new income and expense records (thinkink Tkinter or 
     other Python GUI framework)
