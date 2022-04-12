"""
* Criar variáveis para nome (str), idade (int) *

* altura (float) e peso (float) de uma pessoa *

* criar uma variável com o ano atual (int) * 

* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual) *

* Obter o IMC da pessoa com 2 casas decimais (peso e altura da pessoa) *

* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)

imput

:.2f

"""
nome = str('Higor')

idade = int(20)

altura = float(1.76)

peso = float(95.500)

ano = int(2022)

ano_nascimento = (ano - idade)

imc = peso / (altura ** 2)

print(f'{nome} tem {idade} anos, seu peso atual é de {peso}KG, sua altura é de {altura}m, seu imc atual é: {imc:.2f}, estamos no ano de {ano}, ele nasceu em {ano_nascimento}')


 # FEITO EM 10 MIN.