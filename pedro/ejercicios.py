
import abc


def espaciosguiones(cadena):
    salida = cadena.replace(" ","-")
    return (salida)

def mayuminu(cadena):
    salida = cadena.swapcase()
    return (salida)

def cambiarletra(cadena,letra,indice):
    salida = cadena[:indice]+letra+cadena[(indice+1):]
    return (salida)

def mayunombre(cadena):
    palabras=cadena.rsplit(" ")
    salida=""
    for i in palabras:
        salida = salida + i.capitalize() + " "
    return (salida)

def mayunombre2(cadena):
    palabras=cadena.rsplit(" ")
    for i in range(len(palabras)):
        palabras[i] = palabras[i].capitalize()
    salida = " ".join(palabras)
    return (salida)

def mayunombre3(cadena):
    salida = cadena.title()
    return(salida)

def segundo(puntajes):
    puntajes.sort(reverse=True)
    primero = puntajes[0]
    for i in puntajes:
        if i < primero:
            segundo=i
            break
    return ("el puntaje del subcampeón es ", segundo)

def triangulonumeros(numero):
    i = 1
    while i <= numero:
        lista = []
        for j in range(i):
  	        lista.append(str(i))
        salida = "".join(lista)
        print(salida)
        i += 1

def contarletras(cadena):
    primero = ["0",0]
    segundo = primero
    tercero = primero

    minusculas = cadena.lower()
    for i in range (ord("a"),ord("z")+1):
        x = minusculas.count(chr(i))
        if x > primero[1]:
            tercero = segundo
            segundo = primero
            primero = [chr(i),x] 
        elif x > segundo[1]:
            tercero = segundo
            segundo = [chr(i),x]
        elif x > tercero [1]:
            tercero = [chr(i),x]

    print (primero[0],primero[1])
    print (segundo[0],segundo[1])
    print (tercero[0],tercero[1])


#print(espaciosguiones("Hola Mundo como estamos"))

#print(mayuminu("Hola Mundo Como Estamos"))

#print(cambiarletra("Hola Mundo Como Estamos","G",5))

#print(mayunombre("pedro miguel tomiozzo gutierrez fernandez"))

#print(mayunombre2("pedro miguel tomiozzo gutierrez fernandez"))

#print(mayunombre2("pedro miguel tomiozzo gutierrez fernandez"))

#lista = [2,6,10,10,10,7,5,6]
#print(segundo(lista))

#triangulonumeros(9)

contarletras("Pedro Henry Laura Pablo")