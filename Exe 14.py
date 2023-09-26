fruta_estoque = {
    'maçã': 50,
    'banana': 55,
    'pera': 20,
    'uva': 40,
    'morango': 25,
    'mamão': 30,
    'limão': 40,
}

maior = 0
aux = ' '

for fruta, estoque in fruta_estoque.items():
    if maior < estoque:
        maior = estoque
        aux = fruta

print(f"Tem {maior} de estoque de {aux}")
