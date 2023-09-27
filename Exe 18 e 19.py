jogadores_gols = {
    'Cristiano Ronaldo': 780,
    'Lionel Messi': 750,
    'Neymar Jr.': 220,
    'Robert Lewandowski': 660,
    'Karim Benzema': 510,
    'Harry Kane': 400,
    'Kylian Mbappé': 320
}

gols_jogadores = {gol: jogador for jogador, gol in jogadores_gols.items()}
maiores_gols = dict(sorted(gols_jogadores.items()))
novo_jogadores_gols = {jogador: gol for gol, jogador in gols_jogadores.items()}

for jogador, gol in novo_jogadores_gols.items():
    print(f"{jogador}: {gol}")

mais_gols = 0
jogador_gol = ' '

for jogador, gol in novo_jogadores_gols.items():
    if mais_gols < gol:
        mais_gols = gol
        jogador_gol = jogador

print(f"O jogador com mais gols é {jogador_gol}, com {mais_gols} gols!")
