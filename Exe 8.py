contatos = {'enzo': 27988183155, 'helena': 2893223795, 'mariana': 2799075390}

resposta = input("Deseja adicionar um novo contato (sim/não)? ")

if resposta == "sim":
    nome = input("Digite o nome: ")
    telefone = int(input("Digite o telefone: "))
    
    contatos[nome] = telefone
    
    for n, t in contatos.items():
        print(f"{n}: {t}")

else:
    print("Ok!")
    
remover_resp = input("Deseja remover um contato (sim/não)? ")

if remover_resp == "sim":
    nome = input("Digite o nome: ")
    
    del contatos[nome]
    
    print("Contatos atualizados!")

else:
    print("Ok!")
