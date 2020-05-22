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

#definindo um arquivo para clientes
fileDB = '/Users/jbaldui/Documents/GitHub/Project_Anchieta/Project_Saito/Jefferson/WIP/Database/Menu'


'''
#verificando se arquivo de banco de dados existe
print(f'Verificando se arquivo {fileDB} existe.')
if not os.path.exists(fileDB):
    print(f'O arquivo: {fileDB} não existe!')
    exit(-1)
else:
    pass
'''


# Criando a base de dados
connection = sqlite3.connect(fileDB)

# Get a cursor object
cursor = connection.cursor()

# Adicionando dados da tabela
def data_entry():
    lista_cli = [('JOSE DA SILVA', 'JUNDIAI', 1500.55),
                 ('ANA MARIA', 'JUNDIAI', 2300.69),
                 ('MARIA DE SOUZA', 'CAMPINAS', 3547.02)]

    cursor.executemany("INSERT INTO cliente(id, nome, cidade, salario) \
                    values (?, ?, ?, ?)", lista_cli)

    tupla_cli = (4, 'ANTONIO LIMA', 'VARZEA PAULISTA', 1346.22)
    cursor.execute("INSERT INTO cliente(id, nome, cidade, salario) \
                    values (?, ?, ?, ?)", tupla_cli)

    connection.commit()
    print('Dados inseridos com sucesso!')


#Chamada da funcao de inserção de dados
data_entry()
