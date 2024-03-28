cadas = input("Deseja cadastrar um produto? [Sim/Não]: ").upper()

produtos = []
produtos_e_valores = []
valor = 0
dispo = 0

while cadas == "SIM":
    print("----- CADASTRO -----")
    nome_produto = input("Nome do Produto: ").upper()

    while nome_produto == "":
        print("Digite o nome do produto!")
        nome_produto = input("Nome do Produto: ").upper()

    desc_produto = input("Descrição do Produto: ")

    while True:
        valor_produto = input("Informe o valor do produto: R$")
        try:
            numero = float(valor_produto)
            break
        except ValueError:
            print("Valor inválido! Por favor, informe números.")

    dispo_venda = input("Disponível para venda? [Sim/Não]: ").strip().upper()
    while True:
        if dispo_venda == "SIM":
            produtos_e_valores.append((nome_produto, valor_produto))
            break
        else:
            print("Por favor, só digite Sim ou Não.")
            dispo_venda = input("Disponível para venda? [Sim/Não]: ").strip().upper()
            break
            
    if dispo_venda == "NÃO" or dispo_venda == "NAO":
        print("Produto Indisponível!")      

    while True:
        nova = input("Deseja realizar um novo cadastro? [Sim/Não]: ").strip().upper()
        if nova == "SIM" or nova == "NÃO" or nova == "NAO":
            break
        else:
            print("Digite somente: [Sim ou Não]")

    if nova != "SIM":
        break

print("----- LISTAGEM -----")
if cadas != "SIM":
    print("Nenhum produto cadastrado!")
else:
    produtos_e_valores.sort(key=lambda x: x[1])  # Ordena os produtos pelo seu valor
    print("Produtos cadastrados: ")
    print("(Nome - Valor)")
    for nome_produto, valor_produto in produtos_e_valores:
        print(f"{nome_produto} - R${valor_produto}")