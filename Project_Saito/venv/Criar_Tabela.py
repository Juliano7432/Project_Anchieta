"""
Start Data - 19/05/2020
Project Name - Pizzaria de la puta que lo pario
File - Main.py
Authors - Jefferson Balduino // Victor Machado // Henrique Mariano

Changes Log - 05/19/2020 - R01 - File Created
"""

import os
import sqlite3

#define DB client
fileDB = '/Users/jbaldui/Documents/GitHub/Project_Anchieta/Project_Saito/data/Test_DB'

#

#valida se eu tenho o arquivo ou nao
print('Excluindo o arquivo de banco de dados, caso exista.')
if os.path.exists(fileDB):
    os.remove(fileDB)
else:
    print(f'O arquivo: {fileDB} nao existe!')

#cria a table
print(f'Criando um arquivo {fileDB}')
connection = sqlite3.connect(fileDB)

#cria o cursor object
cursor = connection.cursor()

#criacao da tabelas
def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS cliente \
                   (id     integer PRIMARY KEY, \
                    nome   varchar(40),\
                    cidade varchar(30), \
                    salario decimal(10,2) )'
                   )
create_table()


"""
def main():
    menuPrincipal()


def menuPrincipal():
    print('Main Menu')
    print('1 - Add New Item')
    print('2 - Edit Existing Item')
    print('3 - Help')
    print('Type your option: ')
    selection = int(input())


if __name__ == '__main__':
    main()

"""
