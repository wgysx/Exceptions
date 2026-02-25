def dobro(x):
    return float(x) * 2

valor = input("Digite um número: ")
if valor == "":
    valor = None

print(dobro(valor))