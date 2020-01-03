### budget_tracker

Small Python project.

Using Kivy, sqlite3, and my desire to subconsciously push myself towards
better financial management I am developing a budget tracking app.

My initial intention to use tkinter was a bust. tkinter is a great library for
much simpler implementations than what I had in mind. Kivy seems to be a great fit.
It's cross-platform compatibility sounds like a solid segue into an Android app
at a later date.

I also realize now that an embedded DB is what I need and will revisit PostgreSQL
when I make a web app version of this project.

This application will allow me to grow in areas such as GUI development, DB management
and SQL scripting (with attention paid to secure and best practices.
 
 Features to be implemented:

    -graphical representation of income and spending trajectories
     (Likely to be included in the openpyxl portion of the project)

    -multi-view using Kivy's screenmanager to switch between record
     types (Income/Expense)

    -add/remove/update records

    -date range to view records that fall between dates x and y

    -multi-user support with authentication
    (reserved for web app implementation)

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