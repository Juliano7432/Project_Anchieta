"""
Data........: 2020-25-05
Projeto.....: Pizzaria Bobs
Arquivo.....: Create_Menu.Py
Descrição...: Main Menu for Selection
Autor.......: Jefferson, Henrique, Victor e Juliano
Observações.: Poderia ser bem mais facil
"""

import os
import sqlite3

fileDB = '/Users/jbaldui/Documents/GitHub/Project_Anchieta/Project_Saito/Jefferson/WIP/Project_001/Database/MENU'

print(f'Check if the DB: {fileDB} exists.')
if os.path.exists(fileDB):
    os.remove(fileDB)
else:
    print(f'File: {fileDB} not found!')

print(f'Creating DB @ {fileDB}')
connection = sqlite3.connect(fileDB)

cursor = connection.cursor()

def Create_Mable():
    cursor.execute('CREATE TABLE IF NOT EXISTS MENU \
                   (ID      integer PRIMARY KEY AUTOINCREMENT, \
                    TYPE    varchar(10), \
                    PIZZA  varchar(15), \
                    INGREDIENTS varchar(120),\
                    STD_PRICE decimal (10,2),\
                    MED_PRICE decimal (10,2),\
                    LRD_PRICE decimal (10,2),\
                    SUP_PRICE decimal (10,2) )'
                   )
Create_Mable()
