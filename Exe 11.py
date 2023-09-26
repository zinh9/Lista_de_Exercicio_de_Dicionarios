pais_capital = {
    'Brasil': 'Brasília',
    'Estados Unidos': 'Washington, D.C.',
    'França': 'Paris',
    'Japão': 'Tóquio',
    'Alemanha': 'Berlim',
    'Reino Unido': 'Londres',
    'Austrália': 'Canberra'
}

resposta_usu = input("Digite o país que deseja saber a capital: ")

for pais, capital in pais_capital.items():
    if resposta_usu == pais:
        print(f"A capital de {pais} é {capital}")
        break

else:
    print("O país não está no dicionário!")
