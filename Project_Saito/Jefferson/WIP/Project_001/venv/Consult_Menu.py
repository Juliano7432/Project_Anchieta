"""
Data........: 2020-05-08
Projeto.....: Projeto02 - Manipulacao de Dados com Python e SQLite
Arquivo.....:inserirCliente.py
Descrição...: Faz a inserção de dados na tabela cliente
Autor.......: Rodrigo Saito
Observações.: 2020-05-08 - [R00] Criação do Arquivo - Versao 1.00
              ...
Referencias: https://docs.python.org/2/library/sqlite3.html
"""
import os
import sqlite3
#import Numpy as np

#definindo um arquivo para clientes
fileDB = '/Users/jbaldui/Documents/GitHub/Project_Anchieta/Project_Saito/Jefferson/WIP/Project_001/Database/Menu'

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

# Adicionando dados da tabela
#Selecionando os dados da tabela

#ID, TYPE, PIZZA, INGREDIENTS, STD_PRICE, MED_PRICE, LRD_PRICE, SUP_PRICE

cursor.execute("SELECT ID, TYPE, PIZZA, INGREDIENTS, STD_PRICE, MED_PRICE, LRD_PRICE, SUP_PRICE from MENU")
user1 = cursor.fetchone() #retrieve the first row
print('\nImpressao de campo a campo')
print('ID:', user1[0]) #Imprime o primeiro campo
print('TYPE', user1[1]) #Imprime o segundo campo
print('PIZZA:', user1[2]) #Imprime o terceiro campo
print('INGREDIENTS:', user1[3]) #Imprime o quarto campo
print('STD_PRICE:', user1[4]) #Imprime o quarto campo
print('MED_PRICE:', user1[5]) #Imprime o quarto campo
print('LRD_PRICE:', user1[6]) #Imprime o quarto campo
print('SUP_PRICE:', user1[7]) #Imprime o quarto campo

print('\nImpressao de toda as tuplas')
all_rows = cursor.fetchall()
for row in all_rows:
    #row[0] retorna a primeira coluna da query (id),
    #row[1] retorna a segunda coluna (nome)
    print('{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}, {8}'.format(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
