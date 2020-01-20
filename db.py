import os
import sqlite3

from random import choice


class BudgetDB:

    def __init__(self):

        self.dbpath = "records.db"
        if not os.path.exists(self.dbpath):
            # Creates file in parent directory
            self.__create_db()

    def __create_db(self):
        def __create_expense_table(cur: sqlite3.Cursor):
            cur.execute('''CREATE TABLE Expense
                        ([id] INTEGER PRIMARY KEY,
                        [R_Type] TEXT DEFAULT 'exp',
                        [Date] DATE,
                        [Expense] TEXT,
                        [Cost] DOUBLE)''')

        def __create_income_table(cur: sqlite3.Cursor):
            cur.execute('''CREATE TABLE Income
                        ([id] INTEGER PRIMARY KEY,
                        [R_Type] TEXT DEFAULT 'inc',
                        [Date] DATE,
                        [Source] TEXT,
                        [Amount] DOUBLE)''')

        conn = sqlite3.connect(self.dbpath)
        cur = conn.cursor()
        __create_expense_table(cur)
        __create_income_table(cur)
        self.__close_connection(cur, conn)

    def __connect_db(self):
        if os.path.exists(self.dbpath):
            return sqlite3.connect(self.dbpath)
        else:
            raise FileExistsError(f"No file found in path: ./",
                                  f"Missing file: {self.dbpath}")

    def __close_connection(self, cur: sqlite3.Cursor,
                           conn: sqlite3.Connection):
        if cur:
            cur.close()
        else:
            print("Warning: No cursor defined.")

        if conn:
            conn.close()
        else:
            print("Warning: No connection defined.")

    def get_database(self):
        return self.__connect_db()

    def new_exp_record(self, date: str, expense: str, cost: str):
        """Takes values of new record as arguments.

        Parameters:
        date (str): yyyy-mm-dd
        expense (str): Description of expense
        cost: String value of expense (eg. "45.50")
        cur: Receives cursor object from decorator

        Returns:
        None:
        """

        date = str(date)
        expense = str(expense)
        cost = str(cost)

        # ToDo:
        """SCRUB INPUT BEFORE EXECUTING IT
        """

        conn = self.__connect_db()
        cur = conn.cursor()

        cur.execute(f"""INSERT INTO Expense (Date, Expense, Cost)
        VALUES ("{date}", "{expense}", "{cost}")""")

        conn.commit()
        self.__close_connection(cur, conn)

    def new_inc_record(self, date: str, source: str, amount: str):
        """Takes values of new record as arguments.

        Parameters:
        date (str): yyyy-mm-dd
        source (str): Description of source
        amount: String value of source (eg. "45.50")

        Returns:
        None:
        """

        date = str(date)
        source = str(source)
        amount = str(amount)

        # ToDo:
        """SCRUB INPUT BEFORE EXECUTING IT
        """

        conn = self.__connect_db()
        cur = conn.cursor()

        cur.execute(f"""INSERT INTO Income (Date, Source, Amount)
        VALUES ("{date}", "{source}", "{amount}")""")

        conn.commit()
        self.__close_connection(cur, conn)

    def get_last_x_records(self, amount: int, r_type: str):
        """Returns the most recent records.

        Parameters:
        amount (int): Number of records to retrieve
        r_type (str): "exp" or "inc"

        Returns:
        records (list): List of the last x records
        """

        conn = self.__connect_db()
        cur = conn.cursor()

        if r_type.upper() == "EXP":
            cur.execute('''SELECT R_Type, Date, Expense, Cost FROM Expense''')
        if r_type.upper() == "INC":
            cur.execute('''SELECT R_Type, Date, Source, Amount FROM Income''')

        records = cur.fetchmany(amount)
        self.__close_connection(cur, conn)
        return records

    def get_records_range(self, begin_date: str, end_date: str, r_type: str):
        """Takes date range to retrieve records.

        Parameters:
        begin_date (str): yyyy-mm-dd
        end_date (str): yyyy-mm-dd
        r_type (str): "inc" or "exp"


        Returns:
        records (list): List of records between begin_date and end_date
        """

        conn = self.__connect_db()
        cur = conn.cursor()

        if r_type.upper() == "EXP":
            cur.execute('''SELECT R_Type, Date, Expense, Cost FROM Expense
                        WHERE Date BETWEEN ? and ?''',
                        (begin_date, end_date))

        if r_type.upper() == "INC":
            cur.execute('''SELECT R_Type, Date, Source, Amount FROM Income
                        WHERE Date BETWEEN ? and ?''',
                        (begin_date, end_date))

        records = cur.fetchall()
        self.__close_connection(cur, conn)
        return records


def function_tests():

    test_dates = ["2016-07-10",
                  "2016-04-15",
                  "2016-05-23"]

    test_expenses = ["Groceries",
                     "Takeout",
                     "Gas"]

    test_values = [100.00,
                   45.00,
                   33.76]

    testing = BudgetDB()
    for i in range(50):
        testing.new_exp_record(choice(test_dates),
                               choice(test_expenses),
                               choice(test_values))

    for i in range(50):
        testing.new_inc_record(choice(test_dates),
                               choice(test_expenses),
                               choice(test_values))

    records = testing.get_last_x_records(5, "inc")
    records_range = testing.get_records_range(
                                        "2016-03-01", "2016-08-09", "exp")
    for r in records:
        print(r)

    print()
    print()

    for r in records_range:
        print(r)


if __name__ == "__main__":
    function_tests()
