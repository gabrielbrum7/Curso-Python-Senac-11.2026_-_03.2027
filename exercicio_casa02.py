#Peça um número e diga se ele é positivo, negativo, ou zero.

numero = float(input("Digite um número: "))

if numero > 0:
    print("O número é positivo.")
elif numero == 0:
    print("O número é zero.")
else:
    print("O número é negativo.")