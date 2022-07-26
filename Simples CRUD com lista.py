def menu():
    print("")
    print("Menu")
    print("")
    print("1- Cadastrar produto na lista")
    print("2- Consultar produto na lista")
    print("3- Remover produto da lista")
    print("4- Alterar produto da lista")
    print("5- Sair da lista")
    print("")


print("Lista de Compras")
menu()
escolha = int(input("Escolha uma opção: "))
lista = []
while escolha != 0:

    if escolha == 1:
        produto = str(input("Digite nome do produto, para cadastrar: "))
        if produto.isdigit() == True:
            print("Produto inválido! Não foi cadastrado!")
        else:
            lista.append(produto)
            print("Produto cadastrado!")

    elif escolha == 2:
            for procurar in lista:
                print("Itens na lista: ", lista)
                break

    elif escolha == 3:
            removerProduto = str(input("Digite nome do produto, para remover: "))
            for i in range(len(lista)):
                if lista[i] == removerProduto:
                    lista.remove(removerProduto)
                    print("Produto removido!")
                    break
                else:
                    print("Produto não encontrado!")

    elif escolha == 4:
            contador=0
            alterarProduto= str(input("Digite o nome do produto: "))
            for i in range(len(lista)):
                contador= contador + 1
                if lista[i] == alterarProduto:
                    novoProduto= str(input("Digite nome do novo produto: "))
                    lista[i] = novoProduto
                    print("Alteração efetuada!")
                else:
                    print("Produto não encontrado!")

    elif escolha == 5:
        print("Fim do programa! @Developer Valmir Júnior")
        break

    else:
        print("Escolha inválida, tente novamente")
    menu()
    escolha = int(input("Escolha uma opção: "))
