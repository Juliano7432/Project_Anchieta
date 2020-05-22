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

#definindo um arquivo para clientes
fileDB = '/Users/jbaldui/Documents/GitHub/Project_Anchieta/Project_Saito/Jefferson/WIP/Database/Menu'

#excluindo o arquivo de banco de dados
print(f'Check if the DB: {fileDB} exists.')
if os.path.exists(fileDB):
    os.remove(fileDB)
else:
    print(f'File: {fileDB} not found!')

# Criando a base de dados
print(f'Creating DB @ {fileDB}')
connection = sqlite3.connect(fileDB)

# Get a cursor object
cursor = connection.cursor()

#Criacao de tabelas
def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS cliente \
                   (ID      integer PRIMARY KEY AUTOINCREMENT, \
                    TYPE    varchar(10), \
                    PIZZA  varchar(15), \
                    INGREDIENTS varchar(120),\
                    STD_PRICE decimal (10,2),\
                    MED_PRICE decimal (10,2),\
                    LRD_PRICE decimal (10,2),\
                    SUP_PRICE decimal (10,2) )'
                   )
create_table()