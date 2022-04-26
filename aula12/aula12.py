"""
Formatando valores com modificadores - aula 5
    
:s - texto (strings)
    
:d - Inteiros (int)
    
:f - numeros de ponto flutuante (float)
    
:.(NÚMERO)f - Quantidade de casas decimais (float)
    
:(CARACTERE) (> OU < OU ^) (QUANTIDADE) (TIPO - s, d ou f)
    
> - Esquerda
    
< - Direita
    
^ - Centro
    
"""
    
num_1 = 1
print(f'{num_1:0>10}')
    
    
    
num_2 = 1150
print(f'{num_2:0<10}')
