def sem_repeticao(cidade_estado):
    estados_sem_repeticao = []
    
    for cidade, estado in cidade_estado.items():
        if estado not in estados_sem_repeticao:
            estados_sem_repeticao.append(estado)
    
    return estados_sem_repeticao

cidades_estados = {
    'São Paulo': 'SP',
    'Rio de Janeiro': 'RJ',
    'Belo Horizonte': 'MG',
    'Salvador': 'BA',
    'Recife': 'PE',
    'Fortaleza': 'CE',
    'Manaus': 'AM',
    'Porto Alegre': 'RS',
    'Curitiba': 'PR',
    'Brasília': 'DF',
    'Vitória': 'ES',
    'Guarulhos': 'SP',
}

estados_sem_repeticao = sem_repeticao(cidades_estados)

for estado in estados_sem_repeticao:
    print(estado)
