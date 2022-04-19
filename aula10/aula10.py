# len quatidade de caracteres

from sys import intern

"""
usuario = input('Digite seu nome')
qtd_caracteres = len(usuario)

if qtd_caracteres < 6:
    print('Voce precisa digitar pelo menos 6 caracteres')
else:
    print('Voce foi cadastrado no sistema.')    
    
"""

string1 = input('Digite alguma coisa:')
string2 = input('Digite alguma coisa:')

print(f'A quantidade total de caracteres digitados foi {len(string1) + len(string2)}')