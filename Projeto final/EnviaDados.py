from BinarySearchTree import BinarySearchTree
from Jogo import Jogo

def arvoreJogos():
    ignorar_primeiro = False
    ignorar_proximo = []
    info = []
    dados = BinarySearchTree()
    aux = ''   
    with open("computer_games.csv", "r", encoding="utf-8") as ds:
            for linha in ds.readlines():
                try:
                    if ignorar_primeiro == False:
                        ignorar_primeiro = True
                    else:

                        linha_formatada = linha.split(",")
                        for i in range(len(linha_formatada)):
                            if i in ignorar_proximo:
                                continue

                            elif linha_formatada[i][0] == '"':
                                for j in range(i, len(linha_formatada)):
                                    if linha_formatada[j][-1] == '"':
                                        ignorar_proximo.append(j)
                                        aux += linha_formatada[j]
                                        break
                                    else:
                                        ignorar_proximo.append(j)
                                        aux += linha_formatada[j]
                                formato = aux.strip('"').rstrip("\n").strip('"')
                                info.append(formato)
                                aux = ''
                            else:
                                formato = linha_formatada[i].strip('"').rstrip("\n").strip('"')
                                info.append(formato)
                        
                        jogo = Jogo(info[0], info[1], info[2], info[3], info[4], info[5])
                        dados.add(jogo)
                        info = []
                        ignorar_proximo = []

                except RecursionError:
                    dados.buildTree()
                    continue

    return dados

# Chamar a função e imprimir a árvore
tree = arvoreJogos()
print(tree.search("Transformice"))
