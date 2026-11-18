'''
Calcule, classifique e mostre o IMC
(Abaixo, Normal, Sobrepeso, Obesidade)
IMC = peso/altura²
'''

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso/(altura ** 2)

if imc < 18.5:
    print(f"Classificação do IMC, {imc:.1f}: Abaixo do peso.")
elif imc < 25:
    print(f"Classificação do IMC, {imc:.1f}: Peso normal.")
elif imc < 30:
    print(f"Classificação do IMC, {imc:.1f}: Sobrepeso.")
elif imc < 35:
    print(f"Classificação do IMC, {imc:.1f}: Obesidade grau I.")
elif imc < 40:
    print(f"Classificação do IMC, {imc:.1f}: Obesidade grau II.")
else:
    print(f"Classificação do IMC, {imc:.1f}: Obesidade grave, grau III.")

