nome_idade = {'enzo': 18, 'mariana': 18, 'filipe': 27}

nome_usu = input("Digite o nome para consultar a idade: ")
achei = True

for nome, idade in nome_idade.items():
    if nome == nome_usu:
        print(f"{nome} tem {idade} anos")
        break
    
    else:
        achei = False

if achei == False:
    print("O nome não está no dicionário!")
    
