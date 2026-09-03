from mod_rh import cadastrar_colaborador, exibir_colaboradores

lista_colaboradores = []

while True:
    print("\n=== Sistema de RH ===")
    print("1 - Cadastrar colaborador")
    print("2 - Listar colaboradores")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        nome = input("Nome: ").strip()
        cargo = input("Cargo: ").strip()
        try:
            salario = float(input("Salário: ").strip().replace(",", "."))
        except ValueError:
            print("Salário inválido. Tente novamente.")
            continue

        colaborador = cadastrar_colaborador(nome, cargo, salario)
        lista_colaboradores.append(colaborador)
        print(f"Colaborador '{nome}' cadastrado com sucesso!")

    elif opcao == "2":
        exibir_colaboradores(lista_colaboradores)

    elif opcao == "0":
        print("Saindo do sistema. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
