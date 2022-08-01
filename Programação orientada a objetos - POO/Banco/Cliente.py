class Cliente:
    def __init__(self, n, numeroConta, novoSaldo):
        self._nome = n
        self._conta = numeroConta
        self._valor = novoSaldo

    # métodos get
    def get_nome(self):
        return self._nome

    # método set
    def set_nome(self, nome):
        self._nome = nome

    # método get
    def get_conta(self):
        return self._conta

    # método set
    def set_conta(self, conta):
        self._conta = conta

    # método get
    def get_valor(self):
        return self._valor

    # método set
    def set_valor(self, valor):
        self._valor = valor
