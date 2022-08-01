class Conta:
    def __init__(self, titular, numero, saldo):
        self.saldo = saldo
        self.numero = numero
        self.titular = titular

        def get_saldo(self):
            return self._saldo

        def set_saldo(self, saldo):
            if(saldo < 0):
                print("Saldo negativo!")
            else:
                self._saldo = saldo
