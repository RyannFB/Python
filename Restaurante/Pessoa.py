class Pessoa():
    def __init__(self, nome:str, dinheiro:float, idade:int=-1):
        assert type(nome) == str or type(idade) == int or type(dinheiro) == float, "Siga a seguinte estrutura: nome:str, dinheiro:float, idade:int"
        self.__nome = nome
        self.__dinheiro = dinheiro
        self.__idade = idade

    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    @property
    def dinheiro(self):
        return self.__dinheiro