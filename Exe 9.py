def media(alunos_nota):
    media = 0
    notas = []
    
    for aluno, nota in alunos_nota.items():
        media += nota
        notas.append(nota)
        
    media /= len(notas)
    
    return media

alunos_nota = {'ricardo': 10, 'enzo': 10, 'mariana': 10, 'kaynan': 8, 'luan': 7.5}
nota_media = media(alunos_nota)

print(f"A media das notas dos alunos é de: {nota_media} pontos")
