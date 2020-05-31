"""
Data........: 2020-25-05
Projeto.....: Pizzaria Bobs
Arquivo.....: New_Client.Py
Descrição...: Add New Client
Autor.......: Jefferson, Henrique, Victor e Juliano
Observações.: Poderia ser bem mais facil
"""

import os
import sqlite3

#definindo um arquivo para clientes
fileDB = '/Users/jbaldui/Documents/GitHub/Project_Anchieta/Project_Saito/Jefferson/WIP/Project_001/Database/CLIENTE'

connection = sqlite3.connect(fileDB)

# Get a cursor object
cursor = connection.cursor()

def main():
    menuPrincipal()

def menuPrincipal():
    print('Inserir nova Pizza')
    print('\nQual o nome da pizza??')
    PizzaName = input()
    print('\nQual o tipo da pizza??')
    PizzaType = input()
    print('\nQuais são os incridientes??')
    Ingredientes = input()
    print('\nQual é o valor dessa pizza (Valor padrão)??')
    Value = float(input())
    print('\n\n\nAs opções abaixo estão corretas?? (Sim/Nao)\n')
    print('Nome da Pizza: ', PizzaName)
    print('Tipo da Pizza: ', PizzaType)
    print('Ingredientes: ', Ingredientes)
    print('Valor Padrão: ', Value)
    print('Valor Média: ', Value*1.15)
    print('Valor Grande: ', Value*1.25)
    print('Valor Super: ', Value*1.35)
    insertdata = input()
    if insertdata == 'Sim':
        recordedval = [(PizzaType,PizzaName,Ingredientes,Value,Value*1.15,Value*1.25,Value*1.35)]
        cursor.executemany("INSERT INTO MENU (TYPE, PIZZA, INGREDIENTS, STD_PRICE, MED_PRICE, LRD_PRICE, SUP_PRICE) \
                        values (:TYPE, :PIZZA, :INGREDIENTS, :STD_PRICE, :MED_PRICE, :LRD_PRICE, :SUP_PRICE)",
                           recordedval)

        connection.commit()
        print('Dados inseridos com sucesso!')

    else:
        main()

if __name__ == '__main__':
    main()
