"""
For in em python
Iterando strings com for
Função range(start=0, stop, step=1)
    
    
"""
"""
texto = 'Python'
    
for letra in (texto):
    print(letra)
"""
"""
                         # começo , até, de um em 1
for numero in range(10): #(5      , 10,           1)
    print(numero)
""" 
"""  
for numero in range(20, 10, -1): 
    print(numero)    
    
for numero in range(0, 100, 8):
    print(numero)    
"""

texto = 'Python'
nova_string = ''

# continue - pula para  o proximo laço
# break - encerra o laço

for letra in texto:
    if letra == 't':
        continue
        nova_string = nova_string + letra.upper()
    elif letra == 'h':
        nova_string += letra.upper()
        break
    else:
        nova_string += letra     
    
print(nova_string)           