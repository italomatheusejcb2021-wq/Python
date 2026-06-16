# Preços dos combustíveis
preco_alcool = 5.69
preco_diesel = 2.96
preco_gasolina = 6.07
preco_gnv = 4.15

# Acumuladores
litros_alcool = litros_diesel = litros_gasolina = litros_gnv = 0
clientes_alcool = clientes_diesel = clientes_gasolina = clientes_gnv = 0

while True:
    print("\n1 - Álcool")
    print("2 - Diesel")
    print("3 - Gasolina")
    print("4 - GNV")
    print("0 - Encerrar o dia")

    opcao = int(input("Escolha o combustível: "))

    if opcao == 0:
        break

    litros = float(input("Quantidade de litros: "))

    if opcao == 1:
        litros_alcool += litros
        clientes_alcool += 1

    elif opcao == 2:
        litros_diesel += litros
        clientes_diesel += 1

    elif opcao == 3:
        litros_gasolina += litros
        clientes_gasolina += 1

    elif opcao == 4:
        litros_gnv += litros
        clientes_gnv += 1

    else:
        print("Opção inválida!")

# Cálculo da arrecadação
total_alcool = litros_alcool * preco_alcool
total_diesel = litros_diesel * preco_diesel
total_gasolina = litros_gasolina * preco_gasolina
total_gnv = litros_gnv * preco_gnv

# Relatório
print("\n===== RELATÓRIO DO DIA =====")

print(f"\nÁlcool:")
print(f"Litros consumidos: {litros_alcool:.2f}")
print(f"Clientes: {clientes_alcool}")
print(f"Valor arrecadado: R$ {total_alcool:.2f}")

print(f"\nDiesel:")
print(f"Litros consumidos: {litros_diesel:.2f}")
print(f"Clientes: {clientes_diesel}")
print(f"Valor arrecadado: R$ {total_diesel:.2f}")

print(f"\nGasolina:")
print(f"Litros consumidos: {litros_gasolina:.2f}")
print(f"Clientes: {clientes_gasolina}")
print(f"Valor arrecadado: R$ {total_gasolina:.2f}")

print(f"\nGNV:")
print(f"Litros consumidos: {litros_gnv:.2f}")
print(f"Clientes: {clientes_gnv}")
print(f"Valor arrecadado: R$ {total_gnv:.2f}")