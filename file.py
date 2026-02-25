try:
    nome_arquivo = input("Digite o nome do arquivo: ").strip()
    
    f = open(nome_arquivo, "r", encoding="utf-8")
    print("Conteúdo do arquivo:")
    print(f.read())
    f.close()
    
except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado")
    
except PermissionError:
    print(f"Erro: Sem permissão para ler o arquivo '{nome_arquivo}'")
    
except IsADirectoryError:
    print(f"Erro: '{nome_arquivo}' é um diretório, não um arquivo")
    
except UnicodeDecodeError:
    print(f"Erro: Não foi possível ler o arquivo (problema de codificação)")
    
except Exception as e:
    print(f"Erro inesperado: {e}")