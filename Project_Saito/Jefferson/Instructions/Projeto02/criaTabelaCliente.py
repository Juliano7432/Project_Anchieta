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
fileDB = 'D:\\PyProjects\Projeto02\data\cliente.sqlite'

#excluindo o arquivo de banco de dados
print('Excluindo o arquivo de banco de dados, caso exista.')
if os.path.exists(fileDB):
    os.remove(fileDB)
else:
    print(f'O arquivo: {fileDB} não existe!')

# Criando a base de dados
print(f'Criado um novo arquivo {fileDB}')
connection = sqlite3.connect(fileDB)

# Get a cursor object
cursor = connection.cursor()

#Criacao de tabelas
def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS cliente \
                   (id      integer PRIMARY KEY, \
                    nome    varchar(40), \
                    cidade  varchar(30), \
                    salario decimal(10,2) )'
                   )
create_table()

