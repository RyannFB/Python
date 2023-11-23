class Pedido():
    def __init__(self, nome:str, pedido:str):
        assert type(nome) == str or type(pedido) == str, "O pedido deve ser composta por palavras."
        self.__nome = nome
        self.__pedido = pedido

    def __str__(self):
        return f"(Nome: {self.__nome}, Pedido: {self.__pedido})"

    def __eq__(self, other):
        if isinstance(other, Pedido):
            return self.__nome == other.__nome and self.__pedido == other.__pedido
        return False

    @property
    def pedido(self)-> str:
        return self.__pedido
    
    @pedido.setter
    def pedido(self, novoPedido)->str:
        assert type(novoPedido) == str, "O pedido deve ser composta por palavras."
        self.__pedido = novoPedido
        return self.__pedido

    @property
    def nome(self) -> str:
        return self.__nome
    
    @nome.setter
    def nome(self, novoNome) -> str:
        assert type(novoNome) == str , "O nome deve ser composta por palavras."
        self.__nome = novoNome
        return self.__nome
