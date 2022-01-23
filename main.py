'''
Author : Programming-Mentality
Project : Currency Converter
date : 23-01-2022  Sunday
'''

import json
import tkinter as tk
import winsound
from tkinter import ttk
from tkinter.messagebox import *
from forex_python.converter import CurrencyRates


class App(tk.Tk):
    list1 = []
    Country_list1 = Country_list2 = amount_Enter1 = result_amount = copy_btn = None

    def __init__(self):
        super().__init__()
        self.From_Country = tk.StringVar()
        self.To_Country = tk.StringVar()
        self.From_amount = tk.DoubleVar()
        self.result_amt = tk.DoubleVar()
        # configure the root window
        self.title('Currency Converter')
        self.geometry('700x470')
        self.resizable(False, False)
        self.columnconfigure(0, weight=5)
        self.columnconfigure(1, pad=10)
        self.rowconfigure(0, weight=5)
        self.rowconfigure(1, pad=10)
        # load widgets
        self.titleFrame()
        self.main_contain()
        self.result()

    def copy_text(self):
        if self.result_amt.get() != 0:
            self.clipboard_clear()
            self.clipboard_append(str(self.result_amt.get()))
            winsound.PlaySound("SystemQuestion", winsound.SND_ALIAS)

    def reset_all(self):
        self.Country_list2.set("")
        self.Country_list1.set("")
        self.result_amt.set(0)
        self.From_amount.set(0)

    def check_error(self):
        if str(self.Country_list1.get()) == "":
            showerror(title='Value Error', message='Please Select Converted From Currency')
            return False

        elif str(self.Country_list2.get()) == "":
            showerror(title='Value Error', message='Please Select Converted To Currency')

        elif self.From_amount.get() <= 0:
            showerror(title='Value Error', message='Enter Value Greater than Zero')
            return False

        elif str(self.Country_list1.get()) == str(self.Country_list2.get()):
            showerror(title='Value Error', message='Both Currencies Are Same\n\tPlease Select Different Currencies ')

        else:
            return True

    def show_result(self):
        if self.check_error():
            from_country_ISO = self.find_ISO(self.From_Country.get())
            To_country_ISO = self.find_ISO(self.To_Country.get())
            c = CurrencyRates()
            re = c.convert(from_country_ISO, To_country_ISO, int(self.amount_Enter1.get()))
            re = round(re, 2)
            showinfo(title='Result',
                     message=f'Converted Amount From {self.From_Country.get()} To {self.To_Country.get()} is {re}')
            self.result_amt.set(re)
        else:
            pass

    def find_ISO(self, cname):
        for i in self.list1:
            if cname == i['Name']:
                return i['ISO_Code']

    def main_contain(self):
        f1 = tk.Frame(self, bg="#ffb7c3", borderwidth=4, width=100)
        f1.pack(fill='x', side=tk.constants.TOP, )

        f1.rowconfigure(0, weight=1, minsize=1)
        f1.rowconfigure(1, weight=2, minsize=1)

        f1.columnconfigure(0, weight=1, minsize=1)
        f1.columnconfigure(1, weight=2, minsize=1)

        # From
        f2 = tk.Frame(f1, bg="#ffb7c3", borderwidth=4, relief="flat", width=100)
        f2.grid(row=1, column=0, sticky='n', pady=20)

        label1 = tk.Label(f2, text="Select Converted From : ", font="Calibre 15 ", background="#ffb7c3")
        label1.pack(anchor='nw')

        self.Country_list1 = ttk.Combobox(
            f2, width=20, textvariable=self.From_Country, font="Calibre 15 ")

        country_name = []
        file = open('Country.json')
        a = json.load(file)
        for i in a:
            self.list1.append(i)
            country_name.append(i['Name'])
            self.Country_list1['values'] = tuple(country_name)

        self.Country_list1.pack(side='right', pady=10)

        f21 = tk.Frame(f1, bg="#ffb7c3", borderwidth=4,
                       relief="flat", width=100)
        f21.grid(row=2, column=0, sticky='n')
        label1 = tk.Label(f1, text="Amount : ",
                          font="Calibre 15 ", background="#ffb7c3")
        label1.grid(row=2, column=0, sticky='e')

        self.amount_Enter1 = ttk.Entry(
            f1, width=20, textvariable=self.From_amount, font="Calibre 15 ")
        self.amount_Enter1.grid(row=2, column=1, sticky='w', pady=20)

        # To
        f3 = tk.Frame(f1, bg="#ffb7c3", borderwidth=4, relief="flat", width=100)
        f3.grid(row=1, column=1, sticky='n', pady=20)

        label1 = tk.Label(f3, text="Select Converted To : ", font="Calibre 15 ", background="#ffb7c3")
        label1.pack(anchor='nw')

        self.Country_list2 = ttk.Combobox(f3, width=20, textvariable=self.To_Country, font="Calibre 15 ")

        country_name = []
        file = open('Country.json')
        a = json.load(file)
        for i in a:
            country_name.append(i['Name'])
            self.Country_list2['values'] = tuple(country_name)

        self.Country_list2.pack(side='right', pady=10)

        f31 = tk.Frame(f1, bg="#ffb7c3", borderwidth=4, relief="flat", width=100)
        f31.grid(row=2, column=1, sticky='n')

    def titleFrame(self):
        f1 = tk.Frame(self, bg="#bcf4de", borderwidth=4, relief="solid", )
        f1.pack(fill="both", side=tk.constants.TOP, ipady=50, )
        label = ttk.Label(f1, text="Currency Converter", font="Calibre 30 bold", background="#bcf4de")
        label.place(relx=.30, rely=.25)

    def result(self):

        f1 = tk.Frame(self, bg="#ffb7c3", borderwidth=4, width=100)
        f1.rowconfigure(0, weight=1, minsize=1)

        f1.columnconfigure(0, weight=2, minsize=2)
        f1.columnconfigure(1, weight=1, minsize=1)
        f1.columnconfigure(2, weight=2, minsize=2)
        f1.pack(fill='both', side=tk.constants.TOP, ipady=20)

        label1 = tk.Label(f1, text="Converted Amount : ", font="Calibre 15 ", background="#ffb7c3")
        label1.grid(row=0, column=0, sticky='e')
        self.result_amount = ttk.Entry(f1, width=20, textvariable=self.result_amt, font="Calibre 15 ", state='disabled')
        self.result_amount.grid(row=0, column=1, sticky='w')
        self.copy_btn = tk.Button(f1, text="Copy ", font="Calibre 12 ", bg="#bcf4de", padx=20, relief='solid',
                                  borderwidth=1, command=self.copy_text)
        self.copy_btn.grid(row=0, column=2, sticky='w')

        f2 = tk.Frame(self, bg="#ffb7c3", borderwidth=4)
        f2.pack(fill='both', side=tk.constants.TOP, ipady=5)
        f1.rowconfigure(0, weight=1, minsize=1)

        f2.columnconfigure(0, weight=2, minsize=2)
        f2.columnconfigure(1, weight=1, minsize=1)

        resetbtn = tk.Button(f2, text="Reset", font="Calibre 20 bold", bg="#ff8282", padx=20, relief='solid',
                             borderwidth=1, command=self.reset_all)
        resetbtn.grid(row=1, column=0, sticky='n', pady=10)
        submitbtn = tk.Button(f2, text="Convert", font="Calibre 20 bold", bg="#bcf4de", padx=20, relief='solid',
                              borderwidth=1, command=self.show_result)
        submitbtn.grid(row=1, column=1, sticky='n', pady=10)


if __name__ == "__main__":
    app = App()
    app.mainloop()
