import tkinter as tk


root = tk.Tk(className=" Budget Tracker")
root.minsize(height=600, width=800)


window_ht = int(root.winfo_screenheight() * 0.8)
window_wth = int(root.winfo_screenwidth() * 0.8)

main_canv = tk.Canvas(root, height=window_ht, width=window_wth)
main_canv.pack(fill='both', expand='yes')

# ----------------- TOP FRAME to contain Income/Expense/Balance frames that can be toggled by clicking tabs ------------
# ----------------- Will contain the records ---------------------------
top_frame = tk.Frame(main_canv)
top_frame.place(relheight=0.6, relwidth=0.95, relx=0.025, rely=0.01)


income_frame = tk.Frame(top_frame, bd=2, bg='#bbedbb', relief='groove')
income_frame.pack(fill='both', expand='yes')  # INCOME will be default view

expense_frame = tk.Frame(top_frame, bd=2, bg='red', relief='groove')
balance_frame = tk.Frame(top_frame, bd=2, bg='#4287f5', relief='groove')


# --------------- TOP FRAME TOGGLE BUTTONS ---------------

radio_frame = tk.Frame(top_frame, bd=2, bg='white')
radio_frame.pack(side='bottom')

radio_var = tk.IntVar()
current_sel = radio_var.get()


def top_sel():
    selected = radio_var.get()
    if selected == 0:
        expense_frame.pack_forget()
        balance_frame.pack_forget()
        income_frame.pack(fill='both', side='top', expand='yes')

    if selected == 1:
        income_frame.pack_forget()
        balance_frame.pack_forget()
        expense_frame.pack(fill='both', side='top',  expand='yes')

    if selected == 2:
        income_frame.pack_forget()
        expense_frame.pack_forget()
        balance_frame.pack(fill='both', side='top',  expand='yes')


r_income = tk.Radiobutton(radio_frame, text='Income', variable=radio_var, value=0, command=top_sel)
r_income.pack(side='left')
r_income.select()

r_expense = tk.Radiobutton(radio_frame, text='Expense', variable=radio_var, value=1, command=top_sel)
r_expense.pack(side='left')

r_balance = tk.Radiobutton(radio_frame, text='Balance', variable=radio_var, value=2, command=top_sel)
r_balance.pack(side='left')

# ---------------END OF TOP FRAME ------------------------

# # ----------------- Frame for total values
# middle_frame = tk.Frame()
#
#
# # ----------------- Frame for various buttons that will change based on active tab
# button_frame = tk.Frame()
#
#
# left = tk.Label(labelframe, text="Inside the LabelFrame")
# left.pack()

# Screen height/width divided by 2 gets me to the middle of the screen.
# The req height/width adjust the position based on the minimum required. (Use req dim from main_canv)
# dimensions for the programs window
# -------- Will need to include fix for multi-monitor setup ------
pos_right = root.winfo_screenwidth() // 2 - main_canv.winfo_reqwidth() // 2
pos_down = root.winfo_screenheight() // 2 - main_canv.winfo_reqheight() // 2
root.geometry(f"+{pos_right:}+{pos_down:}")

root.mainloop()
