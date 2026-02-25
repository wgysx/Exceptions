import requests

try:
    nome = input("Pokémon: ").strip().lower()
    if not nome: raise ValueError("Nome vazio")
    
    r = requests.get(f"https://pokeapi.co/api/v2/pokemon/{nome}", timeout=10)
    r.raise_for_status()
    d = r.json()
    
    print(f"\nNome: {d['name'].capitalize()}")
    print(f"ID: #{d['id']}")
    print(f"Tipos: {', '.join([t['type']['name'] for t in d['types']])}")
    
except requests.exceptions.ConnectionError:
    print("Erro: Sem internet")
except requests.exceptions.Timeout:
    print("Erro: Tempo esgotado")
except requests.exceptions.HTTPError as e:
    print("Não encontrado" if r.status_code == 404 else f"Erro HTTP {r.status_code}")
except (ValueError, KeyError, requests.exceptions.JSONDecodeError):
    print("Erro: Dados inválidos")
except Exception as e:
    print(f"Erro: {e}")