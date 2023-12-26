from Pilha import Pilha, PilhaException

class HistorySearchException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class HistorySearch:
    def __init__(self, limit=5):
        self.__pilha = Pilha()
        self.__limit = limit

    def __str__(self):
        reversed_history = list(reversed(self.get_history()))
        return f'{", ".join(map(str, reversed_history))}'
    
    def add_search(self, search):
        if len(self.__pilha) == self.__limit:
            self.__pilha.desempilha()
        self.__pilha = self.__rearrange_history(search)
        
    def remove_search(self):
        if not self.__pilha.estaVazia():
            self.__pilha.desempilha()

    def get_history(self):
        return list(self.__pilha)

    def __rearrange_history(self, new_search):
        support_pilha = Pilha()
        while not self.__pilha.estaVazia():
            support_pilha.empilha(self.__pilha.desempilha())

        support_pilha.empilha(new_search)
        while not support_pilha.estaVazia():
            self.__pilha.empilha(support_pilha.desempilha())
        return self.__pilha
