from fractions import Fraction

class Fraccion:
    def _init_(self, numerador, denominador):
        self.__numerador = numerador
        self.__denominador = denominador

    def _str_(self):
        return f"{self.__numerador}/{self._denominador}"

    def __reduce(self):
        mcd = self.__gcd(self.__numerador, self.__denominador)
        return self.__numerador // mcd, self.__denominador // mcd

    def __gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def suma(self, otra_fraccion):
        numerador = self.__numerador * otra_fraccion.__denominador + \
                    otra_fraccion.__numerador * self.__denominador
        denominador = self.__denominador * otra_fraccion.__denominador
        reducido = Fraccion(numerador, denominador).__reduce()
        return Fraccion(reducido[0], reducido[1])

    def resta(self, otra_fraccion):
        numerador = self.__numerador * otra_fraccion.__denominador - \
                    otra_fraccion.__numerador * self.__denominador
        denominador = self.__denominador * otra_fraccion.__denominador
        reducido = Fraccion(numerador, denominador).__reduce()
        return Fraccion(reducido[0], reducido[1])

    def multiplicacion(self, otra_fraccion):
        numerador = self.__numerador * otra_fraccion.__numerador
        denominador = self.__denominador * otra_fraccion.__denominador
        reducido = Fraccion(numerador, denominador).__reduce()
        return Fraccion(reducido[0], reducido[1])

    def division(self, otra_fraccion):
        numerador = self.__numerador * otra_fraccion.__denominador
        denominador = self.__denominador * otra_fraccion.__numerador
        reducido = Fraccion(numerador, denominador).__reduce()
        return Fraccion(reducido[0], reducido[1])