filmes_star_wars = {
    'Star Wars: A Vingança dos Sith': 2005,
    'Star Wars: O Ataque dos Clones': 2002,
    'Star Wars: O Despertar da Força': 2015,
    'Star Wars: A Ameaça Fantasma': 1999,
    'Star Wars: Os Últimos Jedi': 2017,
    'Star Wars: O Império Contra-Ataca': 1980,
    'Star Wars: O Retorno de Jedi': 1983,
    'Star Wars: Uma Nova Esperança': 1977,
    'Star Wars: A Ascensão Skywalker': 2019
}

filmes_invertidos = {ano: filme for filme, ano in filmes_star_wars.items()}

filmes_ordenados = dict(sorted(filmes_invertidos.items()))

for ano, filme in filmes_ordenados.items():
    print(f"{filme}: {ano}")
