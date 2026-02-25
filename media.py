while True:
    try:
        qtd = int(input("Quantas notas? "))
        if qtd <= 0:
            print("A quantidade deve ser maior que zero. Tente novamente.")
            continue
        break
    except ValueError:
        print("Erro: Digite um número inteiro válido para a quantidade de notas.")

soma = 0
contador = 0

while contador < qtd:
    try:
        nota = float(input(f"Nota {contador + 1}: "))
        soma += nota
        contador += 1
    except ValueError:
        print("Erro: Digite um número válido para a nota (use ponto como separador decimal).")

try:
    media = soma / qtd
    print(f"\nMédia: {media:.2f}")
except ZeroDivisionError:
    print("Erro: Não é possível calcular a média com zero notas.")