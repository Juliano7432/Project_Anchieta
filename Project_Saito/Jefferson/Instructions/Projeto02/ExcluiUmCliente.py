"""
Data........: 2020-05-08
Projeto.....: Projeto02 - Manipulacao de Dados com Python e SQLite
Arquivo.....: excluiUmCliente.py
Descrição...: Faz a exclusao de um registro na tabela cliente
Autor.......: Rodrigo Saito
Observações.: 2020-05-08 - [R00] Criação do Arquivo - Versao 1.00
              ...
Referencias:
"""

import os
import sqlite3

#definindo um arquivo para clientes
fileDB = 'D:\\PyProjects\Projeto02\data\cliente.sqlite'

#verificando se arquivo de banco de dados existe
print(f'Verificando se arquivo {fileDB} existe.')
if not os.path.exists(fileDB):
    print(f'O arquivo: {fileDB} não existe!')
    exit(-1)
else:
    pass

# Criando a base de dados
connection = sqlite3.connect(fileDB)

# Get a cursor object
cursor = connection.cursor()

print('\nExcluindo um ID especifico')
#Referencia: https://www.pythoncentral.io/introduction-to-sqlite-in-python/
user_id = 2
cursor.execute("DELETE from cliente where id = ?", (user_id,))
connection.commit()

print('\nImpressao de toda as tuplas')
#Referencia: https://www.pythoncentral.io/introduction-to-sqlite-in-python/
cursor.execute("SELECT id, nome, cidade, salario from cliente")
all_rows = cursor.fetchall()
for row in all_rows:
    #row[0] retorna a primeira coluna da query (id),
    #row[1] retina a segunda coluna (nome)
    print('{0}, {1}, {2}, {3}'.format(row[0], row[1], row[2], row[3]))