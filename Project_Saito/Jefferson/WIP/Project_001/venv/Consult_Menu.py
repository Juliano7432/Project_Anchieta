"""
Data........: 2020-25-05
Projeto.....: Pizzaria Bobs
Arquivo.....: Consult_Menu.Py
Descrição...: Main Menu for Selection
Autor.......: Jefferson, Henrique, Victor e Juliano
Observações.: Poderia ser bem mais facil
"""

import os
import sqlite3

#definindo um arquivo para clientes
Path_MENU = '/Users/jbaldui/Documents/GitHub/Project_Anchieta/Project_Saito/Jefferson/WIP/Project_001/Database/MENU'

print(f'Verificando se arquivo {Path_MENU} existe.')
if not os.path.exists(Path_MENU):
    print(f'O arquivo: {Path_MENU} não existe!')
    exit(-1)
else:
    pass

DB_MENU = sqlite3.connect(Path_MENU)
cursor_MENU = DB_MENU.cursor()

def Show_Menu():
    cursor_MENU.execute("SELECT * from MENU")
    #user1 = cursor.fetchone() #retrieve the first row
    myresult = cursor_MENU.fetchall()

    for x in myresult:
            print(x)

if __name__ == '__main__':
    Show_Menu()