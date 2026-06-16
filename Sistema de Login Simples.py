#Sistema de Login Simples

usuario_correto = "italo"
senha_correta = "1234"

tentativas = 3

while tentativas > 0:
    usuario = input("Usuário: ")
    senha = input("Senha: ")

    if usuario == usuario_correto and senha == senha_correta:
        print("Login realizado com sucesso!")
        break

    tentativas -= 1
    print(f"Dados incorretos. Restam {tentativas} tentativas.")

if tentativas == 0:
    print("Conta bloqueada.")