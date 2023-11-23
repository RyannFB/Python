from Restaurante import Restaurante, RestauranteException
from Pessoa import Pessoa
from Pedido import Pedido
from time import sleep

# Paulo = Pessoa("Paulo")
# Julia = Pessoa("Julia")
# Alex = Pessoa("Alex")

def cor_azul(texto):
    return f"\033[94m{texto}\033[0m"
def cor_vermelha(texto):
    return f"\033[91m{texto}\033[0m"

r1 = Restaurante("Delizia di Pasta")
conta_cliente = 0
while True:
    try:

        print(f'''
---------------------------------------------     
                 {cor_vermelha("<< Filas >>")}         
---------------------------------------------
{cor_vermelha("Espera:")}  {r1.espera}      
{cor_vermelha("Preparo:")} {r1.preparo}         
{cor_vermelha("Entrega:")} {r1.entrega}         
---------------------------------------------
({cor_vermelha("e")}) Inserir cliente na fila de atendimento.
({cor_vermelha("c")}) Chamar cliente em espera.
({cor_vermelha("i")}) Iniciar preparo da refeição.
({cor_vermelha("r")}) Realizar entrega do pedido.
({cor_vermelha("q")}) Encerrar programa.
=============================================
''')
        resposta = input("Opção: ").lower()

        if (resposta == "e"):
            conta_cliente += 1
            r1.inserirCliente(conta_cliente)
            print(cor_azul(f"<< Aguarde... você está na {r1.espera.busca(conta_cliente)}a posição no atendimento. Aguarde! >>"))
            sleep(1)
        elif (resposta == "c"):
            if (not r1.espera.estaVazia()):
                nome = input("Informe seu nome: ")
                comida = input("Faça seu pedido: ")
                print(f"Olá, {nome}")
                print(f"Informações do pedido: {comida}")
                conf = input("Confirma o pedido (S/N)? ").upper()
                if (conf == "S" or conf == "SIM" or conf == "SI" or conf == "YES"):
                    pedido = Pedido(nome, comida)
                    r1.realizarPedido(pedido)
                    print("Pedido realizado com sucesso!!! Vamos preparar seu prato.")
                    print(cor_azul(f"<< Seu pedido está na {r1.preparo.busca(pedido)}a posição na fila de preparo e deve estar pronto em {r1.preparo.__len__()*20} min >>"))
                    sleep(1)
                else:
                    print(f"Pedido não confirmado, descartando...")
                    r1.espera.desenfileirar
                    sleep(1)
            else:
                print("A fila está vázia!")
        elif (resposta == "i"):
            if (not r1.preparo.estaVazia()):
                first_pedido = r1.pegarPedidoPreparo()
                print(f"Pedido da vez: {first_pedido.pedido}")
                print(f"Cliente: Sr(a) {first_pedido.nome}:")
                conf = input("Pedido já está pronto para entrega (S/N)? ").upper()
                if (conf == "S"):
                    r1.preparoRefeicao(first_pedido)
                    print(cor_azul(f"<< Seu pedido está na {r1.entrega.busca(first_pedido)}a posição para entrega. É rápido, temos vários entregadores>>"))
                    print(cor_azul(f"<< Total de Pedidos pendente: {r1.entrega.__len__() - 1} >>"))
                    sleep(1)
                else:
                    print(f"Pedido não confirmado, descartando...")
                    sleep(1)
            else:
                print("A fila está vázia!")
        elif (resposta == "r"):
            if (not r1.entrega.estaVazia()):
                first_pedido = r1.entregarPedido()
                print(f"Pedido do(a) Sr(a) {first_pedido.nome} saindo para entrega!!!")
                print(f"{first_pedido.pedido}")
                sleep(1)
            else:
                print("A fila está vázia!")
        elif (resposta == "q"):
            print("Encerrando programa...")
            sleep(1)
            break
    except RestauranteException as re:
        print(re)
    except AssertionError as ae:
        print(ae)
    except BaseException as be:
        print(f"Erro desconhecido! '{be}'")
    except:
        print("Erro desconhecido, iremos tratar em breve!")