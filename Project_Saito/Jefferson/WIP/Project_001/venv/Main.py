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
import Insert_Data
import Consult_Menu

Path_MENU = '/Users/jbaldui/Documents/GitHub/Project_Anchieta/Project_Saito/Jefferson/WIP/Project_001/Database/MENU'
DB_MENU = sqlite3.connect(Path_MENU)
cursor_MENU = DB_MENU.cursor()


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
    print('2 - Add New Pizza')
    print('3 - Show Menu')
    print('4 - Show ALL Requests')
    print('0 - Reset DB - WARNING!!!')
    print('9 - Help')
    print('Type your option: ')
    selection = int(input())
    if selection == 1:
        subOrder()
    elif selection == 2:
        Insert_Data.Insert_Pizza()
    elif selection == 3:
        Consult_Menu.Show_Menu()
    elif selection == 4:
        print('Opcao_4')
    elif selection == 5:
        print('Opcao_5')
    elif selection == 6:
        print('Opcao_6')
    elif selection == 7:
        print('Opcao_7')
    else:
        print('Opcao Invalida!!!')
        menuPrincipal()

if __name__ == '__main__':
    main()