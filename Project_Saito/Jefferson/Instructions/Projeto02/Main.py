"""
Data........: 2020-05-08
Projeto.....: Projeto02 - Manipulacao de Dados com Python e SQLite
Arquivo.....: Main.py - Função Principal contendo menu para chamada das demais funções
Autor.......: Rodrigo Saito
Observações.: 2020-05-08 - [R00] Criação do Arquivo - Versao 1.00
              ...
"""

import os

def main():
    menuPrincipal()

def menuPrincipal():
    print('MENU PRINCIPAL')
    print('1 - Inclusao')
    print('2 - Alteracao')
    print('3 - Consulta')
    print('4 - Exclusão')
    print('Digite a opção: ')
    opcao = int(input())

if __name__ == '__main__': # chamada da funcao principal
    main()

