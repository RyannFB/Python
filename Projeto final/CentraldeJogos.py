from BinarySearchTree import BinarySearchTree
from Jogo import Jogo
from Levenshtein import distance

class CentralDeJogos():
    def __init__(self):
        self.__tree = BinarySearchTree()

    def __len__(self):
        return len(self.__tree)

    def addGame(self, jogo:Jogo):
        self.__tree.add(jogo)

    def find_all_SO(self)-> list:
        so_games = []
        for item in self.__tree:
            aux = item.sistema.lower().split()
            for elemento in aux:
                if (elemento not in so_games):
                    so_games.append(elemento)
        return so_games

    def find_all_year(self)-> list:
        year_games = []
        for item in self.__tree:
            aux = item.data.split("/")
            if (aux[2] not in year_games):
                year_games.append(aux[2])
        return year_games
    
    def find_game_year(self, year:str)-> list:
        year_games = []
        all_years = self.find_all_year()
        if (year in all_years):
            for item in self.__tree:
                aux = item.data.split("/")
                if (aux[2] == year):
                    year_games.append(item)
            return year_games
        else:
            return False
        
    def find_game_SO(self, so:str) -> list:
        so_games = []
        all_so = self.find_all_SO()
        if (so in all_so):
            for game in self.__tree:
                if (so in game.sistema.lower()):
                    so_games.append(game)
            return so_games
        else:
            return False

    def search_game(self, key):
        pesquisar_jogo = Jogo(key)
        case_levenshtein = []
        if (self.__tree.search(pesquisar_jogo)):
            return self.__tree.search(pesquisar_jogo)
        else:
            for item in self.__tree:
                if (distance(item.nome[:3].lower(), key[:3].lower()) == 0):
                    case_levenshtein.append(item)
            return case_levenshtein
    
    def cont_game_per_year(self)->dict:
        years = {}
        for item in self.__tree:
            aux = item.data.split("/")
            if (aux[2] not in years):
                years[aux[2]] = 1
            else:
                years[aux[2]] += 1
        return years

    def cont_so(self)->dict:
        so_cont = {}
        for item in self.__tree:
            aux = item.sistema.split()
            for elemento in aux:
                if (elemento not in so_cont):
                    so_cont[elemento] = 1
                else:
                    so_cont[elemento] += 1
        return so_cont        
        
    def getJogos(self)-> list:
        jogos = []
        for carga in self.__tree:
            jogos.append(carga)
        return jogos

