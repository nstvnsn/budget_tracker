"# budget_tracker" 

Small Python3 project. 

Using tkinter, postgreSQL, and my desire to subconsciously push myself towards
better financial management I am developing a budget tracking app.

This application will allow me to grow in areas such as GUI development, DB management
and SQL scripting (with attention paid to secure practices with input sanitation and the
 like). 
 
 Ideas:
    
    -graphical representation of income and spending trajectories
    -multi-user support with authentication
    -port to a web-app or mobile app in the not too distant future
    



---
###_The following is now but a small feature in the program_
##### The excel workbooks will just serve as a means for 
##### exporting a nice formatted .xlsx file

---

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

    -Add/Remove/Update expense records
    -Add/Remove/Update income records
    -set balance fields to calculated values from expense and income sheets
    -Balance forecasting based on income and expenses over last 30 days
