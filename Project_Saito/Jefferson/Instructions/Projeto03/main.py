"""
Data........: 2020-05-08
Projeto.....: Projeto03
Descricao...: Modelo de estrutura de projeto
Arquivo.....: Main.py - Função Principal contendo menu para chamada das demais funções
Autor.......: Rodrigo Saito
Observações.: 2020-05-08 - [R00] Criação do Arquivo - Versao 1.00
              ...
"""

import os

from sources.lib import library

def menuCadastroBasico():
    opcao = 0
    while opcao != 9:
        library.cabecalhoMenu()
        print('Menu de Cadastros Basicos')
        print('[1] - Clientes')
        print('[2] - Pizzas')
        print('[3] - Pedidos')
        print('[9] - Voltar ao menu anterior')
        opcao = eval(input('Digite a opção desejada: '))
        print('Opcao escolhido foi: ', opcao )
        if opcao == 1:
            #torre.menuTorre()
            print('chamada da funcao')
            #break
        elif opcao ==5:
            print('chamada da funcao')
            #contrato.menuContrato()
        else:
            print('Opcao invalida!')


def menuPrincipal():
    opcao = 0
    while opcao != 9:
        library.cabecalhoMenu()
        print('MENU PRINCIPAL')
        print('[1] - Cria base padrão')
        print('[2] - Cadastros básicos')
        print('[3] - Rotinas e manutenções')
        print('[4] - Relatórios em tela')
        print('[9] - Sair')
        opcao = eval(input('Digite a opção desejada: '))
        print('Opcao escolhido foi: ', opcao)

        if opcao == 1:
            print('Fazer a funcao 1')
        #    menuCriaBasePadrao()
        elif opcao == 2:
            menuCadastroBasico()
        elif opcao == 3:
            print('Fazer a funcao 3')
        #    menuRotinasManutencoes()
        else:
            print('Opcao invalida!')

def main():
    menuPrincipal()

if __name__ == '__main__': # chamada da funcao principal
    main()

