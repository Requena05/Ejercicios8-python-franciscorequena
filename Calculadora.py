class Calculadora:
    def __init__(self,numero1=0,numero2=0):

        self.numero1=numero1
        self.numero2=numero2
    @staticmethod
    def sumar(numero1 ,numero2):
        resultado= numero1+numero2

        return resultado

    @staticmethod
    def restar(numero1, numero2):
        resultado = numero1 - numero2

        return resultado

    @staticmethod
    def multiplicar(numero1, numero2):
        resultado = numero1 * numero2

        return resultado

    @staticmethod
    def dividir(numero1, numero2):
        resultado = numero1 / numero2

        return resultado
