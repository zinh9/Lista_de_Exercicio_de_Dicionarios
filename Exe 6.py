compras_valor = {}

while True:
    compra = input("Digite a compra (digite 0 se quiser parar de adicionar): ")
    
    if compra == '0':
        break
    
    valor = float(input("Digite o valor da compra: "))
    
    compras_valor[compra] = valor

valor_total = 0

for compra, valor in compras_valor.items():
    valor_total += valor

print(f"O valor total das compras é de: R${valor_total}")
