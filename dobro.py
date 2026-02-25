def dobro(x):
    try:
        return float(x) * 2
    except (TypeError, ValueError):
        return None

valor = input("Digite um número: ")

if valor == "":
    valor = None

resultado = dobro(valor)

if resultado is not None:
    print(f"O dobro é: {resultado}")
else:
    print("Erro: Valor inválido para cálculo")