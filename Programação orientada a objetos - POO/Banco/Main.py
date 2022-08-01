class Main:
    pass
    print("Banco - Só dinheiro")
    print(" ")
    from Cliente import Cliente
    from Conta import Conta

    nomeTitular = str(input("Digite seu nome: "))
    numeroConta = str(input("Digite o número da conta: "))
    depositar = str(input("Digite quanto deseja depositar: R$"))

    c1 = Cliente(nomeTitular, numeroConta, depositar)

    banco = Conta(c1.get_nome(), c1.get_conta(), c1.get_valor())

    print("Titular da conta: ", banco.titular, ", Número da conta: ", banco.numero, ", saldo= R$", banco.saldo)
