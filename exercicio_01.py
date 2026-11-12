#Crie variáveis com nome, idade e cidade e exiba em uma frase.

'''
Minha reprodução do exercício

nome = "Gabriel"
idade = 33
cidade = "São Gonçalo"

print("Olá, me chamo " + nome + " tenho " + str(idade) + " anos " + "e moro em " + cidade + ".")

'''

#Aula 02 - Reprodução do professor

nome = "Ana"
idade = 25
cidade = "Niterói"

#CTRL + K + C para comentar a(s) linha(s) selecionada(s) || CTRL + K + U para descomentar a(s) linha(s) selecionada(s).

print("Nome", nome)
print("Idade", idade)
print("Cidade", cidade)

#Texto em uma única linha com valores e variáveis. (f-string)
print(f"O nome é {nome}, idade é {idade} anos e mora em {cidade}")

#Usando o (.format), ao invés do f-string.
print("O nome é {}, idade é {} anos e mora em {}".format(nome, idade, cidade))

