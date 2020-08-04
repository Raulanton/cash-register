import tkinter as tk
from tkinter.ttk import *
import sqlite3

#Opens a new window with add and clear buttons
def AddItem():
    windowAdd = tk.Tk()
    windowAdd.title("Add Item")
    windowAdd.geometry("300x300")

    #Takes the parameters from Entry AddItem and add them it to database products (name and price)
    def add():
        newItem = item.get()
        newItemPrice = price.get()
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
    item.place(x=120, y=35, width=50, height=25)
    Label(windowAdd, text = "Product item: ").place(x = 30, y = 100)
    price = Entry(windowAdd, text = "")
    price.place(x = 120, y = 100, width = 50, height = 25)

#Opens new window
def DelItem():
    windowDel = tk.Tk()
    windowDel.title("Delete Item")
    windowDel.geometry("300x300")
    #Search for item (Entry box) in database Items and deletes it
    def delete():
        delitem = item.get()
        cursor.execute("DELETE FROM Items WHERE product=?", (delitem,))

    Button(windowDel, text="Delete", command=delete).place(x=30, y=130)
    Label(windowDel, text="Delete product: ").place(x=30, y=35)
    item = tk.Entry(windowDel, text="")
    item.place(x=120, y=35, width=50, height=25)

#Display database Items
def ShowItems():
    cursor.execute("SELECT * FROM Items")
    data = cursor.fetchall()
    print(data)

#Deletes all items in database Items
def DelAll():
    cursor.execute('DELETE FROM Items;', )

with sqlite3.connect("Items.db") as db:
    cursor = db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS Items(
product text PRIMARY KEY,
  price text); """)

window = tk.Tk()
window.title("cashRegister")
window.geometry("550x400")


buttonAdd = Button(window, text ="Add", command = AddItem)
buttonAdd.place(x = 30, y = 20, width = 100, height = 25)
buttonDelete = Button(window, text ="Delete", command = DelItem)
buttonDelete.place(x = 160, y = 20, width = 100, height = 25)
buttonItems = Button(window, text = "Show items", command = ShowItems)
buttonItems.place(x = 290, y = 20, width = 100, height = 25)
buttonReset = Button(window, text ="Delete All", command = DelAll)
buttonReset.place(x = 420, y = 20, width = 100, height = 25)

tk.mainloop()
db.close()