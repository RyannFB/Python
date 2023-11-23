class Data:
    
    __validação = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    def __init__(self, dia:int, mes:int, ano:int):
        assert ano > 0 , 'Ano digitado está incorreto! O ano tem que ser maior que zero.'
        assert mes >= 1 and mes <= 12, 'Mes inválido! Digite um mês válido ( Entre 1 e 12)'
        assert dia >= 1 and dia <= Data.__validação[mes], f'Dia inserido não está contido no mês {mes}'

        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    def __str__(self):
        return f'{self.__dia}/{self.__mes}/{self.__ano}'
    
    #Métodos getter e setter
    def set_dia(self,dia):
        assert dia >= 1 and dia <= Data.__validação[self.__mes], f'Dia inserido não está contido no mês {self.__mes}'
        self.__dia = dia
    
    def set_mes(self,mes):
        assert self.__dia >= 1 and self.__dia <= Data.__validação[mes], f'Dia inserido não está contido no mês {mes}'
        assert mes >= 1 and mes <= 12, 'Mes inválido! Digite um mês válido ( Entre 1 e 12)'
        self.__mes = mes
    
    def set_ano(self,ano):
        assert ano > 0 , 'Ano digitado está incorreto! O ano tem que ser maior que zero.'
        self.__ano = ano
    
    @property
    def dia(self):
        return self.__dia
    @property
    def mes(self):
        return self.__mes
    @property
    def ano(self):
        return self.__ano