
    

nome = input('Nome: ') # str

idade = input('Qual a sua idade: ') # int

altura = input('Informe a sua altura com ponto: ' ) # float

peso = input('Informe o seu peso com ponto: ' ) # float

imc = float(peso) / (float(altura) * float(altura)) # Formula
# nao  definir o operador da variavel pelo codigo
  
# criar uma somente para a conversao. ex peso = float()

# Resultante IMC

if imc < 17:
    print(f'{nome} o seu indice de massa corporal está muito abaixo do recomendado, e o seu imc é: {imc:.2f}')
elif 17 <= imc < 18.49:
    print(f'{nome} o seu indice de massa corporal está abaixo do recomendado, e o seu imc é: {imc:.2f}')
elif 18.50 <= imc < 24.99:
    print(f'{nome} o seu indice de massa corporal está normal, e o seu imc é: {imc:.2f}')
elif 25 <= imc < 29.99:
    print(f'{nome} o seu indice de massa corporal é considerado acima do peso recomendado, e o seu imc é: {imc:.2f}')
elif 30 <= imc < 34.99:
    print(f'{nome} o seu indice de massa corporal é considerado obesidade I, e o seu imc é: {imc:.2f}')
elif 35 <= imc < 39.99:
    print(f'{nome} o seu indice de massa corporal é considerado obesidade II, e o seu imc é: {imc:.2f}')
elif imc > 40:
    print(f'{nome} o seu indice de massa corporal é considerado obesidade III, e o seu imc é: {imc:.2f}')
     
     
"""
# Tabela IMC
nivel = if imc >= 17
muito_abaixo = imc >= 17
abaixo = imc = 17 >= 18.49
normal = imc = 18.5 >= 24.99
Acima_do_peso = imc = 25 >= 29.99 
obesidade_1 = imc = 30 >= 34.99
obesidade_2 = imc = 35 >= 39.99
Obesidade_3 = imc < 40
"""

 
 
