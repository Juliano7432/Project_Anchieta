"""
Data........: 2020-25-05
Projeto.....: Pizzaria Bobs
Arquivo.....: Consult_Menu.Py
Descrição...: Main Menu for Selection
Autor.......: Jefferson, Henrique, Victor e Juliano
Observações.: Poderia ser bem mais facil
"""

import os
import sqlite3
import Main

#definindo um arquivo para clientes
Path_MENU = '/Users/jbaldui/Documents/GitHub/Project_Anchieta/Project_Saito/Jefferson/WIP/Project_001/Database/MENU'
Path_CUSTOMERS = '/Users/jbaldui/Documents/GitHub/Project_Anchieta/Project_Saito/Jefferson/WIP/Project_001/Database/CUSTOMERS'
Path_ORDERS = '/Users/jbaldui/Documents/GitHub/Project_Anchieta/Project_Saito/Jefferson/WIP/Project_001/Database/ORDERS'

DB_MENU = sqlite3.connect(Path_MENU)
DB_CUSTOMERS = sqlite3.connect(Path_CUSTOMERS)
Path_ORDERS = sqlite3.connect(Path_ORDERS)

# Get a cursor object
cursor_MENU = DB_MENU.cursor()
cursor_CUSTOMERS = DB_CUSTOMERS.cursor()
cursor_ORDERS = Path_ORDERS.cursor()

def Show_Menu():
    cursor_MENU.execute("SELECT * from MENU")
    #user1 = cursor.fetchone() #retrieve the first row
    myresult = cursor_MENU.fetchall()
    for x in myresult:
        print(x)

    Main.menuPrincipal()

def Show_Customers():
    cursor_CUSTOMERS.execute("SELECT * from CUSTOMERS")
    #user1 = cursor.fetchone() #retrieve the first row
    myresult = cursor_CUSTOMERS.fetchall()

    for x in myresult:
        print(x)

def Show_Orders():
    cursor_ORDERS.execute("SELECT * from ORDERS")
    #user1 = cursor.fetchone() #retrieve the first row
    myresult = cursor_ORDERS.fetchall()

    for x in myresult:
        print(x)

if __name__ == '__main__':
    Show_Menu()