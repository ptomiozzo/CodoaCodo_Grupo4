class Complejo:
    def __init__(self, real, imaginario):
        self.real = real
        self.imaginario = imaginario

    def sumar(complejo1, complejo2):
        real =  complejo1.real + complejo2.real
        imaginario = complejo1.imaginario + complejo2.imaginario
        return Complejo(real, imaginario)

    def restar(complejo1, complejo2):
        real =  complejo1.real - complejo2.real
        imaginario = complejo1.imaginario - complejo2.imaginario
        salida = Complejo(real, imaginario)
        return (salida)

    def multiplicar(complejo1, complejo2):
        """(a+bi)(c+di) = ac+adi+bci+bdi2  donde i2= -1
 
                                  = ac+(ad+bc)i -bd
                                 = ac-bd+(ad+bc)i
        """
        unoR = complejo1.real * complejo2.real
        dosI = complejo1.real * complejo2.imaginario
        tresI = complejo1.imaginario * complejo2.real
        cuatroR = complejo1.imaginario * complejo2.imaginario * -1
        real = unoR+cuatroR
        imaginario = dosI+tresI
        salida = Complejo(real, imaginario)
        return (salida)