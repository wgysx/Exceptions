nome_arquivo = input("Arquivo: ")
f = open(nome_arquivo, "r", encoding="utf-8")
print(f.read())
f.close()