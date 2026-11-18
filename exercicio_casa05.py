# Solicite a idade e diga se é criança, adolescente ou adulto.
'''
Minha resolução

idade = int(input("Digite a sua idade: "))

if idade < 12:
    print("Você é uma criança.")
elif (idade >= 12) and (idade < 18):
    print("Você é um adolescente.")
else:
    print("Você é um adulto.")
'''

#Resolução do professor

idade = int(input("Digite sua idade: "))

if idade < 12:
    print("é uma criança!")
elif idade < 18:
    print("Adolescente")
else:
    print("Adulto")