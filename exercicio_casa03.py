'''
Calcule, classifique e mostre o IMC
(Abaixo, Normal, Sobrepeso, Obesidade)
IMC = peso/altura²
'''

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso/(altura * altura)

if imc < 18.5:
    print(f"Classificação do IMC, {imc:.1f}: Abaixo do peso.")
elif imc <= 24.9:
    print(f"Classificação do IMC, {imc:.1f}: Peso normal.")
elif imc <= 29.9:
    print(f"Classificação do IMC, {imc:.1f}: Sobrepeso.")
elif imc <= 34.9:
    print(f"Classificação do IMC, {imc:.1f}: Obesidade grau I.")
elif imc <= 39.9:
    print(f"Classificação do IMC, {imc:.1f}: Obesidade grau II.")
else:
    print(f"Classificação do IMC, {imc:.1f}: Obesidade grave, grau III.")