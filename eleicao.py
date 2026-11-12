"""
Aula 02 - Reprodução do professor

regras da eleição
- obrigatório: 18 até 70 anos
- opcional: 16 e 17 anos e maiores de 70 anos
- não pode votar: menor de 16 anos
"""
# Solução 01
idade = int(input("Digite a sua idade: "))
if (idade >= 16 and idade <18) or idade>70:
    print("voto opcional")
elif idade < 16:
    print("Não pode votar")
else:
    print("voto obrigatório")

# Solução 02
# if idade < 16:
#     print("Não pode votar")
# elif idade >=18 and idade <=70:
#     print("É obrigado votar")
# else:
#     print("Voto opcional")