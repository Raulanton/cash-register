import tkinter as tk
from tkinter.ttk import *
import sqlite3

#Opens a new window with add and clear buttons
def AddItem():
    windowAdd = tk.Tk()
    windowAdd.title("Add Item")
    windowAdd.geometry("230x200")

    #Takes the parameters from Entry AddItem and add them it to database products (name and price)
    def add():
        newItem = item.get()
        newItemPrice = int(price.get())
        cursor.execute("""INSERT OR REPLACE INTO Items(product,price)
        VALUES (?,?)""", (newItem,newItemPrice))
        db.commit()

    #Clear entry boxes
    def clearlist():
        item.delete(0,30)
        price.delete(0,30)

    Button(windowAdd, text = "Add", command = add).place(x=30, y = 130)
    Button(windowAdd, text = "Clear", command = clearlist).place(x=30, y = 160)
    Label(windowAdd, text="Product name: ").place(x=30, y=35)
    item = Entry(windowAdd, text="")
    item.place(x=120, y=35, width=80, height=25)
    Label(windowAdd, text = "Product price: ").place(x = 30, y = 70)
    price = Entry(windowAdd, text = "")
    price.place(x = 120, y = 70, width = 80, height = 25)

#Opens new window
def DelItem():
    windowDel = tk.Tk()
    windowDel.title("Delete Item")
    windowDel.geometry("230x150")
    #Search for item (Entry box) in database Items and deletes it
    def delete():
        delitem = item.get()
        cursor.execute("DELETE FROM Items WHERE product=?", (delitem,))
        item.delete(0,30)
        db.commit()

    Button(windowDel, text="Delete", command=delete).place(x=30, y=80)
    Label(windowDel, text="Delete product: ").place(x=30, y=35)
    item = Entry(windowDel, text="")
    item.place(x=120, y=35, width=80, height=25)

#Display database Items in window
def ShowItems():
    cursor.execute("SELECT * FROM Items")
    for x in cursor.fetchall():
        newrecord = str(x[0]) + "    " + str(x[1]) + "£ " + "\n"
        itemswindow.insert(0, newrecord)

#Clears window
def DelAll():
    itemswindow.delete(0, 30)

def SumCalculator():
    total = 0
    newItem = calculatorItem.get()
    cursor.execute("""SELECT price FROM Items WHERE product=?""",[newItem])
    for x in cursor.fetchall():
        price = calculatorwindow.insert(0, x)

with sqlite3.connect("Items.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Items(
product text PRIMARY KEY,
  price integer); """)

window = tk.Tk()
window.title("cashRegister")
window.geometry("550x400")


buttonAdd = Button(window, text ="Add", command = AddItem)
buttonAdd.place(x = 30, y = 20, width = 100, height = 25)
buttonDelete = Button(window, text ="Delete Item", command = DelItem)
buttonDelete.place(x = 160, y = 20, width = 100, height = 25)
buttonItems = Button(window, text = "Show items", command = ShowItems)
buttonItems.place(x = 290, y = 20, width = 100, height = 25)
buttonReset = Button(window, text ="Clear window", command = DelAll)
buttonReset.place(x = 420, y = 20, width = 100, height = 25)

Label(window, text = "Items recorded").place(x = 10, y = 180)
Label(window, text = "Calculator items").place(x=270, y = 180)

Label(window, text = "Calculator:").place(x=10, y =100)
calculatorItem = Entry(window, text = "")
calculatorItem.place(x=10, y = 120, width = 80, height = 25)
buttonAddCaltulator = Button(window, text = "Sum", command = SumCalculator)
buttonAddCaltulator.place(x= 100, y= 120, width = 100, height = 25)



itemswindow = tk.Listbox()
itemswindow.place(x = 10, y =200, width =255, height = 190)

calculatorwindow = tk.Listbox()
calculatorwindow.place(x =270, y =200, width = 265, height = 190 )

tk.mainloop()
db.close()