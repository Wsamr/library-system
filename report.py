import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk
import customtkinter as ctk
import constants as c
import widgets as w
import database as db

class Report(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, fg_color = c.backgroundColor)

        # variables
        combobox_values = (c.report().issued_book, c.report().overdue_book,c.report().returned_book, c.report().added_user, c.report().deleted_user, c.report().updated_user, c.report().added_book, c.report().deleted_book, c.report().updated_book)
        combobox_var = tk.StringVar(value = '')
        start_var = tk.StringVar(value = '')
        end_var = tk.StringVar(value = '')

        self.rowconfigure((0,1,2,3,5), weight = 1, uniform='a')
        self.rowconfigure(4, weight = 5, uniform='a')
        self.columnconfigure(0, weight = 1, uniform='a')
        self.columnconfigure(1, weight = 2, uniform='a')

        # Report Type Dropdown
        tk.Label(self, foreground= c.fontColor, text='Report Type', font=(c.family, 18, 'bold'), bg=c.backgroundColor).grid(row=0, column=0, padx=10, pady=10, sticky='e')
        w.my_combobox(self, combobox_values, combobox_var).grid(row=0, column=1, padx=(10, 200), pady=10, sticky='we')
        # textvariable=report_type_var,

        # Date Range Picker
        tk.Label(self, foreground= c.fontColor, text="Start Date", font=(c.family, 18, 'bold'), bg=c.backgroundColor).grid(row=1, column=0, padx=10, pady=10, sticky='e')
        start_date_entry = w.my_entry_var(self, hint='Enter Start Date (YYYY-MM-DD)', font=(c.family, 16), height=20, variable=start_var)
        start_date_entry.grid(row=1, column=1, padx=(10, 200), pady=10, sticky='we')

        tk.Label(self, foreground= c.fontColor, text="End Date", font=(c.family, 18, 'bold'), bg=c.backgroundColor).grid(row=2, column=0, padx=10, pady=10, sticky='e')
        end_date_entry = w.my_entry_var(self, hint='Enter End Date (YYYY-MM-DD)', font=(c.family, 16), height=20, variable=end_var)
        end_date_entry.grid(row=2, column=1, padx=(10, 200), pady=10, sticky='we')

        # Report View
        report_tree = ttk.Treeview(self, columns=("report_Type", "generated_on", "report_data"), show="headings")
        
        report_tree.heading("report_Type", text="Report Type")
        report_tree.heading("generated_on", text="Generated On")
        report_tree.heading("report_data", text="Report Data")
        
        report_tree.column('report_Type', width = 20)
        report_tree.column('generated_on', width = 20)
        report_tree.column('report_data', width = 550)

        report_tree.grid(row=4, column=0, columnspan=2, padx=50, pady=10, sticky='nsew')

        def export_report():
            file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
            if not file_path:
                return

            with open(file_path, "w") as f:
                for row in report_tree.get_children():
                    values = report_tree.item(row, "values")
                    f.write(",".join(str(v) for v in values if v) + "\n")
            messagebox.showinfo("Export", "Report exported successfully!")


        # Export Button
        export_button = w.my_button(self, text='Export', font=(c.family, 20, 'bold'), command=export_report)
        export_button.grid(row=5, column=0, columnspan=2, pady=10)

        def generate_report():
            report_tree.delete(*report_tree.get_children())
            reports = db.filter_report(report_type=combobox_var.get(), start_date=start_var.get(), end_date=end_var.get())
            for report in reports:
                report_tree.insert('', 'end', values= report[0:3])

        # Generate Report Button
        generate_report_button = w.my_button(self, text='Generate Report', font=(c.family, 20, 'bold'), command=generate_report)
        generate_report_button.grid(row=3, column=0, columnspan=2, pady=10)


    # ! check invalid date
    # try:
    #     start_date_dt = datetime.strptime(start_date, '%Y-%m-%d')
    #     end_date_dt = datetime.strptime(end_date, '%Y-%m-%d')
    # except ValueError:
    #     messagebox.showerror("Invalid Date", "Please enter valid date ranges.")
    #     return report_tree.delete(*report_tree.get_children())