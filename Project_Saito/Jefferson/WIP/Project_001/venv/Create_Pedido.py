"""
Data........: 2020-25-05
Projeto.....: Pizzaria Bobs
Arquivo.....: Create_Cliente.Py
Descrição...: Main Menu for Selection
Autor.......: Jefferson, Henrique, Victor e Juliano
Observações.: Poderia ser bem mais facil
"""

import os
import sqlite3

def create():
    createmenu()

fileMENU = '/Users/jbaldui/Documents/GitHub/Project_Anchieta/Project_Saito/Jefferson/WIP/Project_001/Database/MENU'
fileCLIENTE = '/Users/jbaldui/Documents/GitHub/Project_Anchieta/Project_Saito/Jefferson/WIP/Project_001/Database/CLIENTE'
fileDB = '/Users/jbaldui/Documents/GitHub/Project_Anchieta/Project_Saito/Jefferson/WIP/Project_001/Database/PEDIDO'




def createmenu():
    print(f'Check if the DB: {fileDB} exists.')
    if os.path.exists(fileDB):
        os.remove(fileDB)
    else:
        print(f'File: {fileDB} not found!')

    print(f'Creating DB @ {fileDB}')
    DB_MENU = sqlite3.connect(fileMENU)
    DB_CLIENTE = sqlite3.connect(fileCLIENTE)
    connection = sqlite3.connect(fileDB)

    cursor = connection.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS PEDIDO \
                   (ID      integer PRIMARY KEY AUTOINCREMENT, \
                    DTTM_Stamp      TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,\
                    PIZZA_SIZE       varchar(3), \
                    PIZZA_ID       integer, \
                    CLIENTE_ID       integer, \
                    FOREIGN KEY(PIZZA_ID) REFERENCES MENU(ID), \
                    FOREIGN KEY(CLIENTE_ID) REFERENCES CLIENTE(ID))'
                   )
createmenu()