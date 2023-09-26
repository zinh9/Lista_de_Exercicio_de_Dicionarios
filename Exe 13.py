produto_estoque = {
    'arroz': 280,
    'feijão': 290,
    'macarrão': 150,
    'biscoito': 350,
    'shampoo': 100,
    'condicionador': 50
}

for produto, estoque in produto_estoque.items():
    if estoque < 150:
        print(f"Tem {estoque} {produto} em estoque. Necessita de mais!")
    
    elif estoque == 150:
        print(f"{estoque} {produto} em estoque. Averiguar produto!")
