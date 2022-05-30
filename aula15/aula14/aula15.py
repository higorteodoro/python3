"""
frase = 'Estou criando uma frase contando a quantidade de letras'
tamanho_frase = len(frase)
contador = 0
nova_string = ''

while contador < tamanho_frase:
      nova_string += frase[contador]
      print(nova_string)  
      contador += 1
    
print(nova_string)    
"""

frase = 'Estou criando uma frase contando a quantidade de letras' # Iterável
tamanho_frase = len(frase)
contador = 0
nova_string = ''

# Iteração
while contador < tamanho_frase:
      letra = frase[contador]
      if letra == 'r':
            nova_string += 'R'
      else:  
          nova_string += letra
      contador += 1
    
print(nova_string)    