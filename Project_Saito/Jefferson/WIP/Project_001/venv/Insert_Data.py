"""
Data........: 2020-25-05
Projeto.....: Pizzaria Bobs
Arquivo.....: Main.Py
Descrição...: Main Menu for Selection
Autor.......: Jefferson, Henrique, Victor e Juliano
Observações.: Poderia ser bem mais facil
"""

import os
import sqlite3


def main():
    menuPrincipal()

"""
(ID      integer PRIMARY KEY AUTOINCREMENT, \
                    TYPE    varchar(10), \
                    PIZZA  varchar(15), \
                    INGREDIENTS varchar(120),\
                    STD_PRICE decimal (10,2),\
                    MED_PRICE decimal (10,2),\
                    LRD_PRICE decimal (10,2),\
                    SUP_PRICE decimal (10,2),\
                    DELETED bit() )'
                   )
"""

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
    print('\n\n\nAs opções abaixo estão corretas?? (Y/N)\n')
    print('Nome da Pizza: ', PizzaName)
    print('Ingredientes: ', Ingredientes)
    print('Valor Padrão: ', Value)
    print('Valor Média: ', Value*1.15)
    print('Valor Grande: ', Value*1.25)
    print('Valor Super: ', Value*1.35)
    
    
    
    
if __name__ == '__main__':
    main()
