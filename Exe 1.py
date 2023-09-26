dicionario = {}

for i in range(3):
    chave = input("Digite uma palavra: ")
    valor = input("Dẽ um valor a essa palavra: ")
    
    dicionario[chave] = valor

for chave, valor in dicionario.items():
    print(f"{chave}: {valor}")
