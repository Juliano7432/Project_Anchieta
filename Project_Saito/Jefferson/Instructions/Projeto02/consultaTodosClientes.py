"""
Data........: 2020-05-08
Projeto.....: Projeto02 - Manipulacao de Dados com Python e SQLite
Arquivo.....:consultaTodosRegistros.py
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

#Selecionando os dados da tabela
cursor.execute("SELECT id, nome, cidade, salario from cliente")
user1 = cursor.fetchone() #retrieve the first row
print('\nImpressao de campo a campo')
print('Id:', user1[0]) #Imprime o primeiro campo
print('Nome:', user1[1]) #Imprime o segundo campo
print('Cidade:', user1[2]) #Imprime o terceiro campo
print('Salario:', user1[3]) #Imprime o quarto campo

print('\nImpressao de toda as tuplas')
all_rows = cursor.fetchall()
for row in all_rows:
    #row[0] retorna a primeira coluna da query (id),
    #row[1] retorna a segunda coluna (nome)
    print('{0}, {1}, {2}, {3}'.format(row[0], row[1], row[2], row[3]))


