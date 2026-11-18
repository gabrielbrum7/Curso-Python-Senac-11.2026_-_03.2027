#Receba duas notas e informe: aprovado, recuperação ou reprovado.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2)/2
if media >= 6:
    print(f"Aprovado! Sua média é {media}")
elif media < 5:
    print(f"Reprovado! Sua media é {media}")
else:
    print(f"Recuperação! Sua média é: {media}")