pessoa = {"nome": "João", "idade": 20, "cidade": "São Paulo"}

while True:
    try:
        chave = input(f"Campos: {list(pessoa.keys())}\nEscolha um: ").strip().lower()
        print(f"{chave.capitalize()}: {pessoa[chave]}")
        break
        
    except KeyError:
        print(f"Erro: '{chave}' não existe. Tente novamente.")