"""

Manipulando strings - aula 6
*String indices
*Fatiamento de strings [inicio:fim:passo]
* Funções built-in len ,abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

"""

# positivos    [012345678]
texto         ='Python s2'

print( len(texto) )
# negativo    -[987654321]
print(texto[8]) #cochete acessar o indice

url = 'www.google.com.br/'

print ( url[:-1] )

nova_string = texto[:6]
print(nova_string)

nova_string = texto[7:]
print(nova_string)

nova_string = texto[:-1]
print(nova_string)

nova_string = texto[-9:-3]
print(nova_string)

nova_string = texto[0: :3] # pula caractere
print(nova_string)



