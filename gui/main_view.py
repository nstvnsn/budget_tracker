import tkinter as tk


root = tk.Tk(className=" Budget Tracker")
root.minsize(height=600, width=800)


window_ht = int(root.winfo_screenheight() * 0.8)
window_wth = int(root.winfo_screenwidth() * 0.8)

cnv_main = tk.Canvas(root, height=window_ht, width=window_wth, bg='white')
cnv_main.pack(fill='both', expand='yes')

# ================ TOP FRAME (Income/Expense/Balance frames) ================
# -----------------------Will contain the records ---------------------------
frm_top = tk.Frame(cnv_main, bg='red')
frm_top.place(relheight=0.5, relwidth=0.95, relx=0.025, rely=0.01)

frm_income = tk.Frame(frm_top, bd=2, bg='#bbedbb', relief='groove')
frm_income.place(relheight=0.9, relwidth=1)  # INCOME will be default view

frm_expense = tk.Frame(frm_top, bd=2, bg='red', relief='groove')
frm_balance = tk.Frame(frm_top, bd=2, bg='#4287f5', relief='groove')


# -------------------- FRAME TOGGLE BUTTONS ---------------
# --------------------- BUTTON FUNCTIONS ---------------------

def show_active_frame(btn_callback):
    def wrapper():
        if btn_callback.__name__ == 'show_income_frame':
            print('test')
            clicked = frm_view_buttons.children.get('btn_income')
        elif btn_callback.__name__ == 'show_expense_frame':
            clicked = frm_view_buttons.children.get('btn_expense')
        else:
            clicked = frm_view_buttons.children.get('btn_balance')
            print()

        buttons = frm_view_buttons.children.items()  # returns tuple (name, obj)

        if clicked.cget('relief') == 'sunken':
            return
        else:

            for btn in buttons:
                if btn[1].cget('relief') == 'sunken':
                    btn[1].configure(relief='ridge')
            clicked.configure(relief='sunken')
        btn_callback()
    return wrapper


@show_active_frame
def show_income_frame():
    """
    Clicking 'Income' button displays Expense frame, hiding the other top frames,
    and reflects changes in the buttons. If Expense frame already active, do nothing.
    """
    frm_balance.place_forget()
    frm_expense.place_forget()
    frm_income.place(relheight=0.9, relwidth=1)


@show_active_frame
def show_expense_frame():
    """
    Clicking 'Expense' button displays Expense frame, hiding the other top frames,
    and reflects changes in the buttons. If Expense frame already active, do nothing.
    """

    frm_balance.place_forget()
    frm_income.place_forget()
    frm_expense.place(relheight=0.9, relwidth=1)


@show_active_frame
def show_balance_frame():
    """
    Clicking 'Balance' button displays Expense frame, hiding the other top frames,
    and reflects changes in the buttons. If Expense frame already active, do nothing.
    """

    frm_expense.place_forget()
    frm_income.place_forget()
    frm_balance.place(relheight=0.9, relwidth=1)


# -------------------- BUTTON LAYOUT ---------------------
frm_view_buttons = tk.Frame(frm_top, bd=1, bg='white')
frm_view_buttons.place(relheight=0.1, relwidth=0.4, relx=0, rely=0.9)

btn_income_view = tk.Button(frm_view_buttons, name='btn_income', text='Income', bd=1, relief='ridge',
                            command=show_income_frame)
btn_income_view.place(height=25, width=60, rely=0)
btn_income_view.configure(relief='sunken')

btn_expense_view = tk.Button(frm_view_buttons, name='btn_expense', text='Expense', bd=1, relief='ridge',
                             command=show_expense_frame)
btn_expense_view.place(height=25, width=60, x=62, rely=0)

btn_balance_view = tk.Button(frm_view_buttons, name='btn_balance', text='Balance', bd=1, relief='ridge',
                             command=show_balance_frame)
btn_balance_view.place(height=25, width=60, x=124, rely=0)

print(btn_income_view.cget('text'))

# ================ END OF TOP FRAME (Income/Expense/Balance frames) ================


# -------- Will need to include fix for multi-monitor setup ------
pos_right = root.winfo_screenwidth() // 2 - cnv_main.winfo_reqwidth() // 2
pos_down = root.winfo_screenheight() // 2 - cnv_main.winfo_reqheight() // 2
root.geometry(f"+{pos_right:}+{pos_down:}")

root.mainloop()
