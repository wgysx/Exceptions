try:
    entrada = input("Preço do produto: R$ ").strip()
    
    # Substitui vírgula por ponto para aceitar ambos formatos
    entrada = entrada.replace(',', '.')
    
    preco = float(entrada)
    
    if preco < 0:
        print("Erro: O preço não pode ser negativo")
    else:
        imposto = 1.1
        preco_final = preco * imposto
        print(f"Preço original: R$ {preco:.2f}")
        print(f"Imposto (10%): R$ {preco * 0.1:.2f}")
        print(f"Preço final: R$ {preco_final:.2f}")
        
except ValueError:
    print("Erro: Digite um valor numérico válido")
except KeyboardInterrupt:
    print("\nOperação cancelada pelo usuário")
except Exception as e:
    print(f"Erro inesperado: {e}")