"""
# continue: até ser verdadeiro após passa para outro laço
# break: quando for verdadeiro para


x += 1 # x = x + 1 simplificar o codigo

 While em Python - Aula 7
 Utilizado para realizar ações enquanto
uma condição for verdadeira.
    
Requisitos: Entender condições e operadores.

"""
"""while True: #loop infinito
    nome = input("Qual o seu nome? ")
    print(f'Olá {nome}!')
"""
"""
x = 0
while x < 5:
    print(x)
    x = x + 1
"""  
"""
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        continue 
        
    print(x)
    x = x + 1      
 
x = 0
while x < 10:
    if x == 3:
        x = x + 1
        break 
        
     
    print(x)
    x = x + 1 
"""    
"""
x = 0 # coluna
while x < 10:
    y = 0 # linha

    while y < 5:    
            print(f'({x},{y})')
            y += 1
    x += 1 # x = x + 1

print('Acabou!')
"""
# continue: até ser verdadeiro após passa para outro laço
# break: quando for verdadeiro para

"""
While / Else - aula 8
Contadores
acumuladores

    
    
"""

contador = 1
acumulador = 1


while contador <= 100:
    print(contador, acumulador)
    
    acumulador = acumulador + contador
    contador += 1 