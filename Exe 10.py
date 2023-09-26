dicionario = {
    'sala 3M1': 30,
    'sala 3M2': 27,
    'sala 3M3': 30,
    'sala 3M4': 29,
    'sala 3M5': 25,
}

resposta_usu = input("Digite a sala que deseja verificar quantos alunos tem (ex: sala 3M1): ")

aux = True

for sala, alunos in dicionario.items():
    if resposta_usu == sala:
        print(f"A sala {sala} tem {alunos} alunos")
        break
    
else:
    print("A sala digitada não existe")
