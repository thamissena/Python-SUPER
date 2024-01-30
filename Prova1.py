email = "usuario1@hotmail.com"
senha = "shdh23B."
while True:
    email_digitado = input("Digite seu e-mail:")
    senha_digitada = input("Digite sua senha: ")
    if email== email_digitado  and senha == senha_digitada:
        print ("Login realizado com sucesso!")
        break
    else:
     print("E-mail ou senha incorreto. \n")