"""
Data........: 2020-05-08
Projeto.....: Projeto02 - Manipulacao de Dados com Python e SQLite
Arquivo.....: atualizaCliente.py
Descrição...: Faz a consulta de dados na tabela cliente de todos regitros
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


print('\nAtualizacao de um dado especifico')
user_id = 3
nome_update = 'CARLOS ANDRE'
cursor.execute("UPDATE cliente set nome = ? where id = ?", (nome_update, user_id,))

cursor.execute("SELECT id, nome, cidade, salario from cliente where id = ?", (user_id,))
user = cursor.fetchone()
connection.commit()

print('Id:', user[0])  # Imprime o primeiro campo
print('Nome:', user[1])  # Imprime o segundo campo
print('Cidade:', user[2])  # Imprime o terceiro campo
print('Salario:', user[3])  # Imprime o quarto campo

# Para fechar a conexao
connection.close()