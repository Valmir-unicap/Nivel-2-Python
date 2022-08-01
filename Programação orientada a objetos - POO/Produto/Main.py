# falta consetar a consulta

def menu():
    print("")
    print("Menu")
    print("")
    print("1- Cadastrar produto na lista")
    print("2- Consultar produto na lista")
    print("0- Sair da lista")
    print("")


class Main:
    pass # deixa passar

    from Produto import Produto

    print("")
    print("Mercado")
    menu()
    escolha = int(input("Escolha uma opção: "))
    lista = []

    while escolha != 0:

        if escolha == 1:
            codigo = str(input("Digite o código do produto: "))
            nome = str(input("Digite o nome do produto: "))
            descricao = str(input("Digite a descricão do produto: "))
            preco = str(input("Digite o preço do produto: R$"))
            quantidade = str(input("Digite a quantidade presente no estoque: "))
            c1 = Produto(codigo, nome, descricao, preco, quantidade)
            print("Código do produto: ", c1.get_codigo(), ", nome do produto: ", c1.get_nome(),
                  ", descrição do produto: ", c1.get_descricao(), ", preço deste produto = R$", c1.get_preco(),
                  ", possui no estoque: ", c1.get_estoque(), " unidades.")

            lista.append(c1)

        elif escolha == 2:
            for procurar in lista:
                print("Itens na lista: ", lista)

        else:
            print("Escolha inválida, tente novamente")
        menu()
        escolha = int(input("Escolha uma opção: "))

print("Fim do programa! @Developer Valmir Júnior")
