"""
Data........: 2020-05-08
Projeto.....: Pizzaria Bobs
Arquivo.....: Alterar_pedido.py
Descrição...: Faz a alteração de dados nas tabelas
Autor.......: Juliano, Victor, Jefferson e Henrique
Observações.: Sim poderia ser mais facil
"""
import os
import sqlite3
import numpy as np

#"fileDB = "F:\Downloads\DataBase"

DB_MENU = sqlite3.connect(Path_MENU)
DB_CUSTOMERS = sqlite3.connect(Path_CUSTOMERS)
Path_ORDERS = sqlite3.connect(Path_ORDERS)

# Get a cursor object
cursor_MENU = DB_MENU.cursor()
cursor_CUSTOMERS = DB_CUSTOMERS.cursor()
cursor_ORDERS = Path_ORDERS.cursor()

def insert_pizza():
    print("Inserir uma nova Pizza")
    print("Qual é o tipo da Pizza?")
    tipo_piz=input()
    print("Qual é a data da criação (dd-mm-aaaa)?")
    data_criacao=input()
    print("Qual é o nome da Pizza?")
    nome_piz=input()
    print("Quais são os ingredientes da Pizza?")
    ingredientes=input()
    print("Qual é o valor da Pizza?")
    valor_custo=input()
    print('\n\n\nAs opções abaixo estão corretas?? (Sim/Nao)\n')
    print('Tipo da Pizza: ', tipo_piz)
    print('Data da criação: ', data_criacao)
    print('Nome da Pizza: ', nome_piz)
    print('Ingredientes: ', ingredientes)
    print('Valor do custo: ', valor_custo)
    alterdados = input()

    if alterdados == 'Sim':
        recordedval = [(tipo_piz, data_criacao, nome_piz, ingredientes, valor_custo)]
        cursor_MENU.executemany("INSERT INTO PIZZA (TIPO_PIZ, DATA_CRIACAO, NOME_PIZ, INGREDIENTES, VALOR_CUSTO) \
                VALUES (:TIPO_PIZ, :DATA_CRIACAO, :NOME_PIZ, :INGREDIENTES, :VALOR_CUSTO)", recordedval)

        cursor_MENU.commit()
        print('Dados inseridos com sucesso!')
    else:
        main()


def insert_client():
    print("Cadastrar um novo Cliente!")
    print("Qual é o seu Telefone fixo?")
    tel_fixo = input()
    print("Qual é o seu Telefone celular?")
    tel_cel = input()
    print("Qual é o nome completo do Cliente?")
    nome_cli = input()
    print("Quais é o Endereço do Cliente?")
    endereco = input()
    print("Qual é o número do endereço?")
    nr_end = input()
    print("Qual é o Complemento do endereço?")
    complemento = input()
    print("Qual é o Bairro?")
    bairro = input()
    print("Qual é a Cidade?")
    cidade = input()
    print("Qual é o Estado (UF)?")
    uf = input()
    print("Qual é o CEP?")
    cep = input()

    print('\n\n\nAs opções abaixo estão corretas?? (Sim/Nao)\n')
    print('Telefone fixo: ', tel_fixo)
    print('Telefone Celular: ', tel_cel)
    print('Nome da Cliente: ', nome_cli)
    print('Endereço: ', endereco)
    print('Número do endereço: ', nr_end)
    print('Complemento: ', complemento)
    print('Bairro: ', bairro)
    print('Cidade: ', cidade)
    print('Estado (UF): ', uf)
    print('CEP: ', cep)
    alterdados = input()

    if alterdados == 'Sim':
        recordedval = [(tel_fixo, tel_cel, nome_cli, endereco, nr_end, complemento, bairro, cidade, uf, cep)]
        cursor_MENU.executemany("INSERT INTO CLIENTE (TEL_FIXO, TEL_CEL, NOME_CLI, ENDERECO, NR_END, COMPLEMENTO, BAIRRO, CIDADE, UF, CEP) \
                VALUES (:TEL_FIXO, :TEL_CEL, :NOME_CLI, :ENDERECO, :NR_END, :COMPLEMENTO, :BAIRRO, :CIDADE, :UF, :CEP)", recordedval)

        cursor_MENU.commit()
        print('Dados inseridos com sucesso!')
    else:
        main()

def insert_order():
    print("Cadastrar um novo Pedido!")
    print("")
