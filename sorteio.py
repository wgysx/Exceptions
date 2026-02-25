nomes = ["Arthur", "Gabriel", "Enzo", "Julia"]

try:
    i = int(input("Digite um número (0 a 3) para sortear uma pessoa: "))
    print("Nome:", nomes[i])
    
except ValueError:
    print("Erro: Digite um número inteiro válido")
    
except IndexError:
    print(f"Erro: Digite um número entre 0 e {len(nomes)-1}")