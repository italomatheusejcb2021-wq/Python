# Solicita um número inteiro positivo ao usuário
n = int(input("Digite um número inteiro positivo: "))

# Verifica se o número é positivo
if n < 0:
    print("Por favor, digite um número positivo.")
else:
    # Mostra os números pares de n até 0
    for i in range(n, -1, -1):
        if i % 2 == 0:
            print(i)