from ConversorCSVemLista import converte_csv_em_lista
from CentraldeJogos import CentralDeJogos
from Jogo import Jogo
from time import sleep
from HistoricoSearch import HistorySearch, HistorySearchException


def cor_azul(texto):
    return f"\033[94m{texto}\033[0m"

def cor_vermelha(texto):
    return f"\033[91m{texto}\033[0m"

def exibir_menu_com_historico(history_search):
        print(f'''
{cor_vermelha("================ Menu Principal ===============")}
{cor_azul("(p)")} Pesquisar jogo.                                
{cor_azul("(l)")} Listar os jogos por sistema operacional.        
{cor_azul("(d)")} Listar jogos por ano de lançamento. 
{cor_azul("(y)")} Ver quantos jogos em cada ano.
{cor_azul("(o)")} Ver sistema operacional mais utilizado.  
{cor_azul("(q)")} Quantidade de jogos armazenados.        
{cor_azul("(s)")} Sair.
{cor_vermelha("Histórico de pesquisa: ")}{history_search}
''')

def print_resultado(search:str, jogos:list):
    cont = 0
    print(f'''
Resultados: {search} 
ID  Jogo            Genero            Desenvolvedor 
=== ==============  ================  ================''') 
    for item in jogos:
        cont += 1
        print(f'{cont:03d} {item.nome:<14.14}  {item.genero:<16.16}  {item.desenvolvedor:.16s}')
    sleep(1)


#Necessário a implementação 
        # Quantidade de itens carregados;
#   Quantidade de itens descartados;
#       O Sistema operacional que tem mais títulos de jogos disponíveis;
#           Quantos jogos foram lançados em cada ano, por ordem decrescente de ano. Por exemplo:
                # 1997: 12
                # 1998: 15
                # 1999: 7

# ----------------------------------------------------------------------------------------------------------------------

jogos = converte_csv_em_lista("computer_games.csv")
gamer_center = CentralDeJogos()
history_search = HistorySearch()

for item in jogos:
    game = Jogo(item[0], item[1], item[2], item[3], item[4], item[5])
    gamer_center.addGame(game)

while True:
    try:
        exibir_menu_com_historico(history_search)

        resposta = input("Opção: ").lower()
             
        if (resposta == "p"):
            pesquisa = input("Pesquisar: ")
            jogo_encontrado = gamer_center.search_game(pesquisa)
            if (type(jogo_encontrado) != list):
                print(jogo_encontrado)
            else:
                print_resultado(pesquisa, jogo_encontrado)
            history_search.add_search(pesquisa)
            sleep(2)

        elif (resposta == "l"):
            sistema_operacional = input("Exibir os jogos disponíveis em qual sistema operacional: ").lower()
            so_games = gamer_center.find_game_SO(sistema_operacional)
            if (so_games == False):
                print("Sistema operacional inexistente!")
            else:
                print_resultado(sistema_operacional, so_games)
            history_search.add_search(sistema_operacional)

        elif (resposta == "d"):
            ano_de_lançamento = input("Digite o ano: ")
            year_games = gamer_center.find_game_year(ano_de_lançamento)
            if (year_games == False):
                print("\n| Ano inexistente! |")
                sleep(1)
            else:
                print_resultado(ano_de_lançamento, year_games)
                sleep(1)
            history_search.add_search(ano_de_lançamento)
        
        elif (resposta == "y"):
            cont_year_game = gamer_center.cont_game_per_year()
            cont_year_game = dict(sorted(cont_year_game.items()))
            for chave, carga in cont_year_game.items():
                print(f"{chave}: {carga}")
            sleep(2)

        elif (resposta == "o"):
            cont_so = gamer_center.cont_so()
            print(f"\n| Sistema Operacional mais utilizado: {max(cont_so, key=cont_so.get)} |")
            sleep(2)

        elif (resposta == "q"):
            print(f"\n| Temos {len(gamer_center)} jogos armazenados! |")
            sleep(2)

        elif (resposta == "s"):
            print("Finalizando o programa...")
            sleep(1)
            break     
        else:
            print("\n| Opção inexistente! |")

    except AssertionError as ae:
        print(ae)
    except BaseException as be:
        print(be, "Erro desconhecido, iremos tratar em breve!")
