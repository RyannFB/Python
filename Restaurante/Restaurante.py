from Fila import Fila, FilaException

class RestauranteException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class Restaurante():
    def __init__(self, nome:str, loc:str=any):
        self.__nome = nome
        self.__loc = loc
        self.__espera = Fila()
        self.__preparo = Fila()
        self.__entrega = Fila()

    def __str__(self):
        return f"Nome: {self.__nome}, Localização: {self.__loc}"

    #Insere a posição que está na fila e coloca ele na lista de espera
    def inserirCliente(self, contaCliente:int):
        self.__espera.enfileirar(contaCliente)
        return True

    #Recebe pedido e o nome, tira o cliente da fila de espera e coloca na fila de preparo
    def realizarPedido(self, pedido:object):
        self.__espera.desenfileirar()
        self.__preparo.enfileirar(pedido)
        return True
    
    #Método para consulta os clientes em espera
    @property
    def espera(self):
        return self.__espera

    #Pega o pedido da fila de espera
    def pegarPedidoPreparo(self):
        pedido = self.__preparo.desenfileirar()
        return pedido
    
    #Adiciona o pedido a fila de entrega
    def preparoRefeicao(self, pedido):
        self.__entrega.enfileirar(pedido)
        return True
    
    #Método que consulta os clientes e seus pedidos em preparo 
    @property
    def preparo(self):
        return self.__preparo
    
    #Entrega o pedido e tira ele da fila de entrega
    def entregarPedido(self):
        pedido = self.__entrega.desenfileirar()
        return pedido
    
    #Método que consulta todos os clientes que estão com seus pedidos prontos para entrega
    @property
    def entrega(self):
        return self.__entrega
    
    #Método para desinfileirar advindo da estrutura de dados para fazer a conversação com o main
    def desenfileirar(self):
        return self.__espera.desenfileirar()