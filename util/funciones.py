#1 - Dado un string, escribir una funcion que cambie todos los espacios por guiones.
def reemplazar(texto, caracerOrigen, caracterDestino):
    salida = texto.replace(caracerOrigen, caracterDestino)
    return salida

#2- Cambiar Mayusculas por Minusculas. (Ejemplo: "Hola Mundo" -> "hOLA mUNDO"). 
#Tiene como limite 100 caracteres.     
def mayPorMin(texto):
    return texto.swapcase()

#3- Los strings son inmutables, escribir una funcion que reciba un string,
#   un indice y una letra a modificar de ese string y que devuelve el string modificado.
def cambioLetra(texto, indice, carCambiar):
    if indice > len(texto):
        return 'No se puede'
    else:
        return texto[:indice] + carCambiar + texto[indice+1:]


#4- Escribir una funcion que reciba un string con nombre y apellido y devuelva un string con el nombre 
# y apellido pero con capitalizacion(primera letra mayuscula).        
def primeraLetraMay(texto):
    salida =""
    mayu=True
    for letra in texto:
        #si es el primer caracter o es el siguiente a un blanco paso a mayusculas
        if mayu:
           salida = salida + letra.upper()
        else:
           salida = salida + letra
        if letra == ' ':
            mayu = True
        else:
            mayu = False
    return salida

#5- Escribir una funcion que reciba N numeros, los cuales representan la puntuacion de un concurso, 
# y esta devuelve la puntuacion del subcampeon. (ejemplo de ingreso de datos... 
# [2,6,10,10,7,5,6], debe devolver 7)    
def subCampeon(lista):
    #saco los distintos
    salida= set(lista)
    #paso a lista
    salida = list(sorted(salida))
    return salida[-2]

#Extra: a- Escribir una funcion que recibe un numero entero y imprima por salida estandar(usando print) 
# un triangulo de numeros de altura igual al numero ingresado.
#  Ej. Si se ingresa el numero 5, debe imprimir:    
#1
#22
#333
#4444
#55555
def impTriangulo(numeros):
    for numero in range(numeros):
        otroNum=numero+1
        print (str(otroNum) * otroNum)
    return ''

#b- Escribir una funcion que reciba un string(el cual representara el nombre de una empresa) y
#  devuelve por salida estandar(usando print) los 3 caracteres mas usados en un orden descendiente
# . Ejemplo. "Codo a Codo" Debe imprimir:
# o 4
# c 2
# d 2
def caracterMasUsado(texto, insenCase):
    dicci = {}

    for letra in texto:
        if insenCase:
            #Si no le importa mayusculas o minusculas llevo todo a mayusculas
            letra = letra.lower()

        if letra != ' ':
            if letra not in  dicci:
                dicci[letra] = 1
            else:
                dicci[letra] += 1

    #Se ordena el diccionario usando la funcion lambda
    # exampleDict.items() devuelve una lista de pares clave-valor del diccionario 
    # y el tipo de datos de su elemento es tuple. x es el elemento de esta tupla,
    #  donde x[0] es la clave y x[1] es el valor. key=lambda x:x[1] indica que la clave de comparación 
    # es el valor de los elementos del diccionario.
    """
    dicciOrdenado = sorted(dicci.items(), key=lambda x: x[1], reverse=True)
    conta=1
    for clave in dicciOrdenado:
        conta+=1
        if conta>3:
            break
            print(clave[0],clave[1])
    """

    dicciOrdenado = sorted(dicci.items(), key=lambda x: x[1], reverse=True)
    conta=0
    while conta<=2:
        print(dicciOrdenado[conta][0],dicciOrdenado[conta][1])
        conta+=1

