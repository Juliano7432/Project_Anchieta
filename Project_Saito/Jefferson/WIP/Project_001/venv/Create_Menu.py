"""
Data........: 2020-05-08
Projeto.....: Projeto02 - Manipulacao de Dados com Python e SQLite
Arquivo.....: criaTabelaCliente.py
Descrição...: Faz a criacao da tabela cliente
Autor.......: Rodrigo Saito
Observações.: 2020-05-08 - [R00] Criação do Arquivo - Versao 1.00
              ...
Referencias: https://www.w3schools.com/python/python_file_remove.asp

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
