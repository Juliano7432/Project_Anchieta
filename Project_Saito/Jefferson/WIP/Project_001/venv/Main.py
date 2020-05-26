"""
Data........: 2020-25-05
Projeto.....: Pizzaria Bobs
Arquivo.....: Main.Py
Descrição...: Main Menu for Selection
Autor.......: Jefferson, Henrique, Victor e Juliano
Observações.: Poderia ser bem mais facil
"""

import os
import numpy as np

def main():
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


if __name__ == '__main__':
    main()