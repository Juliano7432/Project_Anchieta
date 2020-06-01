"""
Data........: 2020-25-05
Projeto.....: Pizzaria Bobs
Arquivo.....: Consult_Menu.Py
Descrição...: Main Menu for Selection
Autor.......: Jefferson, Henrique, Victor e Juliano
Observações.: Poderia ser bem mais facil
"""
import os
import sqlite3
#import Numpy as np
#definindo um arquivo para clientes
fileDB = '/Users/jbaldui/Documents/GitHub/Project_Anchieta/Project_Saito/Jefferson/WIP/Project_001/Database/MENU'
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

cursor.execute("SELECT * from MENU")
myresult = cursor.fetchall()
for x in myresult:
   print(x)
