"""
Fazer um programa que peca ao usuario para digitar um numero inteiro,
infome se este numero e par ou impar. Caso o usuario nao digite um numero
inteiro, informe que nao e um numero inteiro.

"""
"""
Faca um programa que pergunte a hora do usuario e, baseando-se no horario
descrito, exiba a saudacao apropriada. EX.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23

"""
"""
fazer um programa que peca o primeiro nome do usuario. Se o nome tiver 4 letras ou
menos escreva "Seu nome e curo"; se tiver entre 5 e 6, escreva "Seu nome e normal";
Maior que 6 escreva "Seu nome e muito grande"

"""
<<<<<<< HEAD
"""
nome = input('Qual o seu nome: ')
num = input('Digite um numero inteiro: ')
num = int()
resultado = num % 2
if resultado == 0:
    print(f'{nome} o numero digitado é {num} esse numero é par')
else:
    print(f'{nome} o numero digitado é {num} esse numero é impar')
"""    
 """       
nome = input('Qual o seu nome: ')
quantidade = len(nome)

if quantidade <= 4:
    print(f'Seu nome é curto')
elif 5 >= quantidade <= 6:
    print(f'Seu nome é normal')
elif quantidade > 6:    
    print(f'Seu nome é normal')
""" 
=======

nome = input('Digite seu nome: ')
hora = float(input(f'Que horas sao {nome}?:'))


if hora <= 11.59:
    print(f'Bom dia {nome}')
elif 12 >= hora > 17.59:
    print(f'Boa tarde {nome}')
elif 18 >= hora < 23.59:
    print(f'Boa noite {nome}')


>>>>>>> c7ae09a098fca64d04a9c44fc3e10c5f8a97b8e9

