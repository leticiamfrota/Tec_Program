class Calculadora:

    def __init__(self):
        self.__acumulador = 0.0

    def soma(self,operando_a, operando_b=None):
        if operando_b is None:
            self.__acumulador = operando_a + self.__acumulador
        else:
            self.__acumulador = operando_a + operando_b
        return self.__acumulador

    def subtracao(self,operando_a, operando_b=None):
        if operando_b is None:
            self.__acumulador = self.__acumulador - operando_a
        else:
            self.__acumulador = operando_a - operando_b
        return self.__acumulador
        
    def multiplicacao(self,operando_a, operando_b=None):
        if operando_b is None:
            self.__acumulador = operando_a * self.__acumulador
        else:
            self.__acumulador = operando_a * operando_b
        return self.__acumulador

    
    def divisao(self,operando_a, operando_b=None):
        if operando_b is None:
            self.__acumulador = self.__acumulador / operando_a
        else:
            self.__acumulador = operando_a / operando_b
        return self.__acumulador

    def get_acumulador(self):
        return self.__acumulador
