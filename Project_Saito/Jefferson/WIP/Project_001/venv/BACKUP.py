"""
Data........: 2020-25-05
Projeto.....: Pizzaria Bobs
Arquivo.....: BACKUP.Py
Descrição...: Main Menu for Selection
Autor.......: Jefferson, Henrique, Victor e Juliano
Observações.: Poderia ser bem mais facil
"""

import os
import sqlite3
#import Numpy as np

#definindo um arquivo para clientes
fileDB = '/Users/jbaldui/Documents/GitHub/Project_Anchieta/Project_Saito/Jefferson/WIP/Project_001/Database/Menu'

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
def data_entry():
    STD_List = [(1, 'Salgada', 'Alho e Óleo', 'Alho Frito Picado, Parmesão Ralado, e Azeitonas', 22.9, 26.33, 28.62, 30.91),
                (2, 'Salgada', 'Aliche', 'Aliche Importado, Rodelas de Tomate, Parmesão e Azeitonas', 28.9, 33.23, 36.12, 39.01),
                (3, 'Salgada', 'Atum', 'Atum, Cebola e Azeitona', 22.9, 26.33, 28.62, 30.91),
                (4, 'Salgada', 'Bacon', 'Bacon Coberto com Muzzarela e Azeitonas', 26.9, 30.93, 33.62, 36.31),
                (5, 'Salgada', 'Berinjela', 'Berinjela, Cobertura com Muzzarela, Manjericão e Parmesão', 23.9, 27.48, 29.87, 32.26),
                (6, 'Salgada', 'Caipira', 'Frango Desfiado, Coberto com Catupiry e Milho Verde e Azeitonas', 26.9, 30.93, 33.62, 36.31),
                (7, 'Salgada', 'Calabresa', 'Linguiça Calabresa, Cebola e Azeitona', 19.9, 22.88, 24.87, 26.86),
                (8, 'Salgada', 'Cinco Quejos', 'Muzzarela, Parmesão, Catupiry, Gorgonzola e Provolone', 29.9, 34.38, 37.37, 40.36),
                (9, 'Salgada', 'Escarola', 'Escarola Refogada, Muzzarela e Azeitonas', 24.9, 26.33, 28.62, 30.91),
                (10, 'Salgada', 'Executiva', 'Milho Verde, Catupiry e Azeitonas', 22.9, 26.33, 28.62, 30.91),
                (11, 'Salgada', 'Peruana', 'Atum, Cebola, Muzzarela e Azeitonas', 26.9, 30.93, 33.62, 36.31),
                (12, 'Salgada', 'Palmito', 'Palmito com Muzzarela e Azeitonas', 26.9, 30.93, 33.62, 36.31),
                (13, 'Doce', 'Banana', 'Banana Fatiada com cobertura de leite condensado e canela em pó', 21.9, 26.33, 28.62, 30.91),
                (14, 'Doce', 'Brigadeiro', 'Chocolate, Leite Condensado e chocolate granulado', 23.9, 27.48, 29.87, 32.26),
                (15, 'Doce', 'Prestigio', 'Chocolate coberta de côco', 23.9, 27.48, 29.87, 32.26)]



    cursor.executemany("INSERT INTO MENU (ID, TYPE, PIZZA, INGREDIENTS, STD_PRICE, MED_PRICE, LRD_PRICE, SUP_PRICE) \
                    values (:ID, :TYPE, :PIZZA, :INGREDIENTS, :STD_PRICE, :MED_PRICE, :LRD_PRICE, :SUP_PRICE)", STD_List)

    connection.commit()
    print('Dados inseridos com sucesso!')


#Chamada da funcao de inserção de dados
data_entry()
