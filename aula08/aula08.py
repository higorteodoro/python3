"""
Operadores relacionais

== Igualdade

> Maior que 

>= Maior igual

< Menor que 

<= Menor igual

!= Diferente
"""
teste = ( 2 * 4 == 4 + 4)

teste2 = ( 4 + 4 == 4 * 2)

expressao = (teste == teste2)
print(expressao)



nome = input('Qual o seu nome? ')

idade = int(input('Qual a sua idade? '))

mjovem = 20

mold = 31

if idade <= mjovem:
    print(f'{nome} no momento não temos nenhum imprestimo para de oferecer.')
elif idade >= mold:
    print(f'{nome} no momento não temos nenhum imprestimo para de oferecer.')
else:
    print(f'{nome} pode pegar o emprestimo')    