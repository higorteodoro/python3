"""
if, elif , else
posso deixar so o if , so elif , nunca so o else
else e executado quando nao existe verdadeiro
"""

if False:
    print('Verdadeiro')
    print('teste teste2')
elif True:
    print("Agora é verdadeiro.")
    nome = input("Qual o seu nome?")

    print(f'Seu nome é {nome}.')
elif False:
    print('Mais uma verdadeira.')
    print(22 + 22)
else:
    print("Não é verdadeiro.")
    print("Olá")        
