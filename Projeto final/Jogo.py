class Jogo():
    def __init__(self, nome:str, desenvolvedor:str="", produtora:str="", genero:str="", sistema:str="", data:str=""):
        assert type(nome) == str and type(desenvolvedor) == str and type(produtora) == str and type(genero) == str and type(sistema) == str and type(data) == str, "Os parâmetros devem ser do tipo str!"
        self.__nome = nome
        self.__desenvolvedor = desenvolvedor
        self.__produtora = produtora
        self.__genero = genero
        self.__sistema = sistema
        self.__data = data

    #Métodos especiais
    def __str__(self):
        return f'''
Nome: {self.nome}
Desenvolvedor: {self.desenvolvedor}
Produtora: {self.produtora} 
Gênero: {self.genero}
Sistema Operacional: {self.sistema}
Criação: {self.data}
'''

    def __eq__(self, other):
        if isinstance(other, Jogo):
            return self.nome.lower() == other.nome.lower()
    
    def __le__(self, other):
        if isinstance(other, Jogo):
            return self.nome.lower() <= other.nome.lower()

    def __gt__(self, other):
        if isinstance(other, Jogo):
            return self.nome.lower() > other.nome.lower()
    
    def __ge__(self, other):
        if isinstance(other, Jogo):
            return self.nome.lower() >= other.nome.lower()

    def __lt__(self, other):
        if isinstance(other, Jogo):
            return self.nome.lower() < other.nome.lower()

    def __ne__(self, other):
        if isinstance(other, Jogo):
            return self.nome.lower() != other.nome.lower()
    
    #Getters
    @property
    def nome(self):
        return self.__nome
    @property
    def desenvolvedor(self):
        return self.__desenvolvedor
    @property
    def produtora(self):
        return self.__produtora
    @property
    def genero(self):
        return self.__genero
    @property
    def sistema(self):
        return self.__sistema
    @property
    def data(self):
        return self.__data