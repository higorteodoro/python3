
nome = input('Nome: ') # str

idade = input('Qual a sua idade: ') # int

altura = input('Informe a sua altura com ponto: ' ) # float

peso = input('Informe o seu peso com ponto: ' ) # float

imc = float(peso) / (float(altura) * float(altura)) # Formula

# Resultante IMC

if imc < 17:
    print(nome, ', O seu indice de massa corporal está muito abaixo do recomendado, e o seu imc é:', imc)
elif 17 <= imc < 18.49:
    print(nome, ', O seu indice de massa corporal está abaixo do recomendado, e o seu imc é:', imc)
elif 18.50 <= imc < 24.99:
    print(nome, ', O seu indice de massa corporal está normal, e o seu imc é:', imc)
elif 25 <= imc < 29.99:
    print(nome, ', O seu indice de massa corporal é considerado acima do peso recomendado, e o seu imc é:', imc)
elif 30 <= imc < 34.99:
    print(nome, ', O seu indice de massa corporal é considerado obesidade 1, e o seu imc é:', imc)
elif 35 <= imc < 39.99:
    print(nome, ', O seu indice de massa corporal é considerado obesidade 2, e o seu imc é:', imc)
elif imc > 40:
    print(nome, ', O seu indice de massa corporal é considerado obesidade 3, e o seu imc é:', imc)
     
     
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

 
 
