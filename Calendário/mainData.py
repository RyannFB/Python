from Data import Data

while True:

    try:
        dia = int(input('Dia: '))
        mes = int(input('Mês: '))
        ano = int(input('Ano '))

        

        data1 = Data(dia, mes, ano)
    except ValueError:
        print('Erro na digitação do dia, mes ou ano')
        continue
    except AssertionError as ae:
        print(ae)
        continue
    except Exception as e:
        print('O sistema esta instável. Nossos desenvolvedores vao corrigir em pouco tempo')
        print(e.__class__.__name__)
        exit()

    break

try:
    print('Data no formato DD/MM/AAAA')
    dia = int(input('Dia:'))
    print('+'*10)
    data1.set_dia(dia)
    mes = int(input('Mes:'))
    print('+'*10)
    data1.set_mes(mes)
    ano = int(input('Ano:'))
    print('+'*10)
    data1.set_ano(ano)
except AssertionError as ae:
    print(ae)

print(data1.dia)
print(data1.mes)
print(data1.ano)

print('Impressão da data: ', data1)