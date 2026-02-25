import requests

nome = input("Digite um número para descobrir o pokemon: ").strip().lower()
url = f"https://pokeapi.co/api/v2/pokemon/{nome}"

resposta = requests.get(url)
dados = resposta.json()

print("Nome:", dados["name"])

## Instale o módulo requests
## No terminal, execute: pip install requests