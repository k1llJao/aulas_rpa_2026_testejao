def cadastrar_colaborador(nome: str, cargo: str, salario: float) -> dict:
    """
    Recebe os dados de um colaborador e retorna um dicionário estruturado.
    """
    colaborador = {
        "nome": nome,
        "cargo": cargo,
        "salario": salario
    }
    return colaborador


def exibir_colaboradores(lista_colaboradores: list) -> None:
    """
    Percorre a lista de colaboradores e imprime cada um formatado.
    """
    if not lista_colaboradores:
        print("Nenhum colaborador cadastrado.")
        return

    print("\n--- Lista de Colaboradores ---")
    for i, colaborador in enumerate(lista_colaboradores, start=1):
        print(f"{i}. Nome: {colaborador['nome']} | Cargo: {colaborador['cargo']} | Salário: R$ {colaborador['salario']:.2f}")
    print("------------------------------")
