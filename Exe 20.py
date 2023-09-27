livros = [
    {
        'titulo': 'Uma Breve História do Tempo',
        'autor': 'Stephen Hawking',
        'ano': 1988
    },
    {
        'titulo': 'O Universo Numa Casca de Noz',
        'autor': 'Stephen Hawking',
        'ano': 2001
    },
    {
        'titulo': 'Uma Nova História do Tempo',
        'autor': 'Stephen Hawking',
        'ano': 2005
    },
    {
        'titulo': 'Relatividade: A Especial e a Geral',
        'autor': 'Albert Einstein',
        'ano': 1916
    },
    {
        'titulo': 'O Significado da Relatividade',
        'autor': 'Albert Einstein',
        'ano': 1922
    },
    {
        'titulo': 'Sobre a Teoria da Relatividade Especial e Geral',
        'autor': 'Albert Einstein',
        'ano': 1917
    },
    {
        'titulo': 'Cosmos',
        'autor': 'Carl Sagan',
        'ano': 1980
    },
    {
        'titulo': 'A Origem das Espécies',
        'autor': 'Charles Darwin',
        'ano': 1859
    },
    {
        'titulo': 'A Dança do Universo',
        'autor': 'Marcelo Gleiser',
        'ano': 1997
    },
    {
        'titulo': 'O Gene Egoísta',
        'autor': 'Richard Dawkins',
        'ano': 1976
    }
]

for i in range(0, len(livros) - 1):
    print("Título: ", livros[i]['titulo'])
    print("Autor: ", livros[i]['autor'])
    print("Ano: ", livros[i]['ano'])
