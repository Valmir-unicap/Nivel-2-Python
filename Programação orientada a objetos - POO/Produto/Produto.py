class Produto:

    def __init__(self, codigo, nome, descricao, preco, estoque): #construtor
        self._codigo = codigo
        self._nome = nome
        self._descricao = descricao
        self._preco = preco
        self._estoque = estoque

    # métodos get
    def get_codigo(self):
        return self._codigo

    # método set
    def set_codigo(self, codigo):
        self._codigo = codigo

    # método get
    def get_nome(self):
        return self._nome

    # método set
    def set_nome(self, nome):
        self._nome = nome

    # método get
    def get_descricao(self):
        return self._descricao

    # método set
    def set_descricao(self, descricao):
        self._descricao = descricao

    # método get
    def get_preco(self):
        return self._preco

    # método set
    def set_preco(self, preco):
        self._preco = preco

    # método get
    def get_estoque(self):
        return self._estoque

    # método set
    def set_estoque(self, estoque):
        self._estoque = estoque
