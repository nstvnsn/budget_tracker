### budget_tracker

To try out main app GUI(Not functional, work in Progress):

1. Clone repo
2. cd to repo directory
3. Run `pip install -r requirements.txt` (Pip required)
4. Run `python3 main.py`


To generate a spreadsheet '.xlsx' file:

1. cd to repo directory (if not already there)
2. Run `python3 excel/output.py`

Small Python project.

Using PyQt5, sqlite3, and my desire to subconsciously push myself towards
better financial management I am developing a budget tracking app.

My aim with this application is to grow in areas such as GUI development, DB management
and SQL scripting.

Features to be implemented:

    -graphical representation of income and spending trajectories
     (Likely to be included in the openpyxl portion of the project)

    -two views for records. An income view and an expense view

    -add/remove/update records

    -date range to view records that fall between dates x and y

    -multi-user support with authentication
    (reserved for web app implementation perhaps)

---

### The following is now but a small feature in the program

Uses openpyxl to create a workbook of spreadsheets.

4 sheets in total:

    -Income
    -Expense
    -Balance
    -Controls

Creates a new workbook with 4 new worksheets in root directory, unless workbook
already in existence.

Income and Expense are styled templates containing field labels that determine
the structure of the records they contain. Balance is another styled template
containing 3 fields storing calculated values. Control is
a sheet reserved for control values that are used, currently empty save for a title
header.

Expense:

    -Date
    -Expense
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

    -implement tables and graphs to visually represent income and spending
