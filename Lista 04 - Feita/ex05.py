print('''=== AGENDA TELEFONICA ===''')
cont = 1
agenda = {}
while cont == 1:
    opcao = int(input("[1] - INSERIR\n[2] - REMOVER\n[3] - PESQUISAR\n[4] - SAIR\nDigite a opção desejada:\n"))
    if opcao == 1:
        nome = input("nome:\n")
        email = input("email:\n")
        telefone = int(input("telefone:\n"))
        endereco = input("endereço:\n")
        agenda[nome] = [email, telefone, endereco]
    elif opcao == 2:
        nome = input("Digite o nome do contato que deseja apagar:\n")
        del agenda[nome]
    elif opcao == 3:
        nome = input("Digite o nome do contato:\n")
        if nome in agenda:
            print(nome)
            c = 0
            for i in agenda[nome]:
                if c == 0:
                    print("E-mail: ", i)
                elif c == 1:
                    print("Telefone: ", i)
                elif c == 2:
                    print("Endereco: ", i)
                c += 1
        else:
            print("Contato nao encontrado.")
    elif opcao == 4:
        print("Fim da Ação.")
        break
    else:
        print("Opcao invalida.")