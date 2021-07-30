import requests as re
import tkinter as tk
from self import self
from tkinter import *
from tkinter import ttk


class CurrencyConverter():

 def __init__(self,url):
    self.data= re.get(url).json()
    self.currencies =self.data['rates']

 
def convert(self, from_currency, to_currency, amount):
    initial_amount =amount
    if from_currency != 'USD':
        amount = amount / self.currencies[from_currency] 
        return amount

class App(tk.Tk):

 def __init__(self, converter):
    tk.Tk.__init__(self)
    self.title ='Currency Converter'
    self.currency_converter = converter
self.geometry("400x200")
self.intro_label =Label(self, txt ='Welcome to real Time Currency converter', fg = 'blue', elief =tk.RAISED, borderwidth =3)               
self.intro_label.config(font =('Courier',15,'bold'))

self.date_label =Label(self, text = f"1 Indian Rupee equals = {self.currency_converter.converter('INR','USD',1)}USD\n Date : {self.currency_converter.data['date']}", relief = tk.GROOVE, borderwidth =5)

self.intro_label.place(x =10,y=5)
self.date_label.place(x =170, y=50)

# entry box

valid =(self.register(self.restrictNumberOnly),'%d', '%f')
self.amount_field = Entry(self,bd =3, relief =tk.RIDGE, justify = tk.CENTER, validate='key',validatecommand=valid)
self.converted_amount_feild_label = Label(self, text ='', fg ='black', bg ='white',relief = tk.RIDGE, justify = tk.CENTER, width = 17, borderwidth =3)

#dropdown

self.from_currency_variable = StringVar(self)
self.from_currency_variable.set("INR") #default value
self.to_currency_variable = StringVar(self)
self.to_currency_variable.set("USD") #default value

font = ("Courier", 12, "bold")
self.option_add('*TCombobox*Listbox.font', font)
self.from_currency_dropdown = ttk.Combobox(self,textvariable=self.from_curency_variable,values=list(self.currency_converte.currencies.keys()),font = font, state = 'readonly', width = 12, justify= tk.CENTER)
self.from_currency_dropdown = ttk.Combobox(self,textvariable=self.to_curency_variable,values=list(self.currency_converte.currencies.keys()),font = font, state = 'readonly', width = 12, justify= tk.CENTER)

#placing

self.from_currency_dropdown.place(x = 30, y= 120)
self.amount_feild.place(x = 36, y =150)
self.to_currency_dropdown.place(x = 340, y= 150)
self.converted_amount_feild_label.place(x =346, y =150)

# convert button

self.convert_button = Button(self, text = "Convert", fg ="black", command =self.perform )
self.convert_button.config(font=('Courier',10, 'bold'))
self.convert_button.place(x = 225, y =135)

def perform(self,) :
    amount =float(self.from_currency_variable.get())
    from_currency = self.from_currency_variable.get()
    to_currency = self.to_currency_variable.get()

    converted_amount = self.currency_converter.convert(from_currency,to_currency,amount)
    converted_amount = round(converted_amount,2)

    self.converted_amount_field_label.config(text = str(converted_amount))

# restrict number only

def restrictNumberOnly(self, action, string):
    regex = re.compile(r"[0-9]*?(\.)[0-9,]*$")
    result = regex.match(string)
    return(string =="" or (string.count('.')<= 1 and result is not None))

if __name__ == '__main__':
    url = 'https://api.exchangerate-api.com/v4/latest/USD'
    converter= CurrencyConverter(url)

App(CurrencyConverter)
mainloop()    
    