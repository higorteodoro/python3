
"""
Formatação de string

F strings

{imc:.2f} 2 casa decimais f = ponto flutuante
"""
nome = "Higor" # str
idade = 20 # int
altura = 1.76 # float
peso = 95.55 # float
imc = peso / (altura ** 2) # formula

    # Forma mais recomendada informando a variavel conforme necessidade.

 print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')

    # utilizando essa forma de formatação de string eu sempre tenho que numerar as variaveis.

 print('{0} tem {1} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))


    # utilizando essa forma de formatação de string eu sempre tenho que nomear as variaveis.

 print('{n} tem {i} anos de idade e seu imc é {:.2f}'.format(n=nome, i=idade, imc))


