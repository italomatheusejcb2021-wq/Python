def area_triangulo(base, altura):
    return (base * altura) / 2
 
def area_circulo(raio):
    return 3.14 * (raio ** 2)
 
def area_losango(diag_maior, diag_menor):
    return (diag_maior * diag_menor) / 2
 
def area_retangulo(base, altura):
    return base * altura
 
def area_trapézio(base_maior, base_menor, altura):
    return ((base_maior + base_menor) * altura) / 2
 
 
print("CÁLCULO DE ÁREAS GEOMÉTRICAS")
print("1 - Triângulo")
print("2 - Círculo")
print("3 - Losango")
print("4 - Retângulo")
print("5 - Trapézio")
op = int(input("Escolha uma opção (1-5): "))
 
if op == 1:
    b = float(input("Digite a base (b): "))
    h = float(input("Digite a altura (h): "))
    print(f"Área do Triângulo: {area_triangulo(b, h):.2f}")
 
elif op == 2:
    r = float(input("Digite o raio (r): "))
    print(f"Área do Círculo: {area_circulo(r):.2f}")
 
elif op == 3:
    D = float(input("Digite a diagonal maior (D): "))
    d = float(input("Digite a diagonal menor (d): "))
    print(f"Área do Losango: {area_losango(D, d):.2f}")
 
elif op == 4:
    b = float(input("Digite a base (b): "))
    h = float(input("Digite a altura (h): "))
    print(f"Área do Retângulo: {area_retangulo(b, h):.2f}")
 
elif op == 5:
    B = float(input("Digite a base maior (B): "))
    b = float(input("Digite a base menor (b): "))
    h = float(input("Digite a altura (h): "))
    print(f"Área do Trapézio: {area_trapézio(B, b, h):.2f}")
 
else:
    print("baka")