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
import Create_Menu


def main():
    menuPrincipal()

def subOrder():
    GerarOrdem()

def GerarOrdem():
    print('Main Menu')
    print('1 - Cliente ja Cadastrado')
    print('2 - Novo Cliente')
    print('Type your option: ')
    selection = int(input())
    if selection == 1:
        print('Chama Funcao Inserir pedido')
    elif selection == 2:
        print('Chama Funcao Inserir Cliente')
    else:
        menuPrincipal()


def menuPrincipal():
    print('Main Menu')
    print('1 - Add New Item')
    print('2 - Show Menu')
    print('3 - Edit Menu')
    print('4 - Show ALL Requests')
    print('0 - Reset DB - WARNING!!!')
    print('9 - Help')
    print('Type your option: ')
    selection = int(input())
    if selection == 1:
        subOrder()
    elif selection == 0:
        Create_Menu.createmenu()
    elif selection == 3:
        print('3 - Edit Menu')
    else:
        menuPrincipal()

if __name__ == '__main__':
    main()