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

fileDB = '/Users/jbaldui/Documents/GitHub/Project_Anchieta/Project_Saito/Jefferson/WIP/Project_001/Database/CLIENTE'

def createmenu():
    print(f'Check if the DB: {fileDB} exists.')
    if os.path.exists(fileDB):
        os.remove(fileDB)
    else:
        print(f'File: {fileDB} not found!')

    print(f'Creating DB @ {fileDB}')
    connection = sqlite3.connect(fileDB)

    cursor = connection.cursor()

'''
ID
Telefone 
Nome
Endereço 
Número 
Complemento 
Bairro
Cidade
UF
CEP
'''

    cursor.execute('CREATE TABLE IF NOT EXISTS MENU \
                   (ID      integer PRIMARY KEY AUTOINCREMENT, \
                    FIRST_NAME     varchar(25), \
                    LAST_NAME      varchar(25), \
                    ADDRESS        varchar(120),\
                    ST_NUM         int(3),\
                    COMPLEMENTO    varchar(30),\
                    BAIRRO         varchar(15),\
                    CIDADE         varchar(15),\
                    UF             varchar(2),\
                    CEP            varchar(9),\
                    DELETED        bit() )'
                   )
createmenu()
