#Verificação de acesso 02
login = input("Digite seu e-mail ou usuário: ").strip().lower() #lower transforma a string caixa alta em caixa baixa.
senha = input("Digite sua senha: ").strip() #Função ou método que remove, ou anula, espaços da string (nas pontas).
print(login)
if login == "ricardoazeredo" and senha == "Python123":
    print("Acesso permitido!")
else:
    print("Usuário e/ou Senha incorreta! Tente novamente.")