def calorias_total(alimento_caloria):
    calorias = 0
    
    for alimento, caloria in alimento_caloria.items():
        calorias += caloria
    
    print(f"A quantidade de calorias consumidas em uma refeição é de: {calorias} cal")

alimento_caloria = {
    'Arroz': 206,
    'Feijão': 89,
    'Frango grelhado': 165,
    'Salada de alface e tomate': 22,
    'Batata frita': 365,
    'Refrigerante': 150,
    'Maçã': 52,
    'Sorvete de chocolate': 143
}
calorias_total(alimento_caloria)
