class complejo:
    def __init__(self,a=0,b=0) -> None:
        self.real = float(a)
        self.imag = float(b)
    
    def __str__ (self):
        return str(self.real) + "+" + str(self.imag) + "j"

    def suma (numcom1, numcom2):
        real = numcom1.real + numcom2.real
        imag= numcom1.imag + numcom2.imag
        return(complejo(real,imag))
    
    def resta (numcom1, numcom2):
        real = numcom1.real - numcom2.real
        imag= numcom1.imag - numcom2.imag
        return(complejo(real,imag))
    
    def producto (numcom1, numcom2):
        real = numcom1.real * numcom2.real - numcom1.imag * numcom2.imag
        imag= numcom1.real + numcom2.imag + numcom1.imag * numcom2.real
        return(complejo(real,imag))
    
    def division (numcom1, numcom2):
        a = numcom1.real
        b = numcom1.imag
        c = numcom2.real
        d = numcom2.imag
        real = (a*c+b*d)/((c**2)-(d**2))
        imag= -(a*d - b*c)/((c**2)-(d**2))
        return(complejo(real,imag))

class vector:
    def __init__(self,x=0,y=0,z=0) -> None:
        self.x = x
        self.y = y
        self.z = z
    
    def __str__ (self):
        return "[" + str(self.x) + "," + str(self.y) + "," + str(self.z) + "]"

    def suma (vector1, vector2):
        x = vector1.x + vector2.x
        y = vector1.y + vector2.y
        z = vector1.z + vector2.z
        return(vector(x,y,z))
    
    def resta (vector1, vector2):
        x = vector1.x - vector2.x
        y = vector1.y - vector2.y
        z = vector1.z - vector2.z
        return(vector(x,y,z))
    
    def prodescalar (vector1, escalar):
        x = vector1.x * escalar
        y = vector1.y * escalar
        z = vector1.z * escalar
        return(vector(x,y,z))
    
    def divescalar (vector1, escalar):
        x = vector1.x / escalar
        y = vector1.y / escalar
        z = vector1.z / escalar
        return(vector(x,y,z))

class matriz: #La matriz está escrita por columnas [x y z], y cada columna es un vector de 3 elementos
    def __init__(self,x=[0,0,0],y=[0,0,0],z=[0,0,0]) -> None:
        self.v1 = vector(x[0],x[1],x[2])
        self.v2 = vector(y[0],y[1],y[2])
        self.v3 = vector(z[0],z[1],z[2])

    def __str__ (self):
        return "[" + str(self.v1) + " " + str(self.v2) + " " + str(self.v3) + "]"

    def suma (A1, A2):
        a = vector.suma(A1.v1, A2.v1)
        b = vector.suma(A1.v2, A2.v2)
        c = vector.suma(A1.v3, A2.v3)
        x = [a.x,a.y,a.z]
        y = [b.x,b.y,b.z]
        z = [c.x,c.y,c.z]
        return (matriz(x,y,z))
    
    def resta (A1, A2):
        a = vector.resta(A1.v1, A2.v1)
        b = vector.resta(A1.v2, A2.v2)
        c = vector.resta(A1.v3, A2.v3)
        x = [a.x,a.y,a.z]
        y = [b.x,b.y,b.z]
        z = [c.x,c.y,c.z]
        return (matriz(x,y,z))
    
    def prodvector(A1, v1):
        a = vector.prodescalar (A1.v1, v1.x)
        b = vector.prodescalar (A1.v2, v1.y)
        c = vector.prodescalar (A1.v3, v1.z)
        x = [a.x,a.y,a.z]
        y = [b.x,b.y,b.z]
        z = [c.x,c.y,c.z]
        return (matriz(x,y,z))


#x = complejo(2.5,4)
#y = complejo(1,5)
#z = complejo.resta(x,y)
#q = complejo.producto(x,y)
#w = complejo.division(x,y)

#print(x)
#print(y)
#print(z)
#print(q)
#print(w)

#x = vector(2.5,4)
#y = vector(1,5,6.3)
#z = vector.suma(x,y)
#q = vector.resta(x,y)
#w = vector.prodescalar(x,4)

#print(x)
#print(y)
#print(z)
#print(q)
#print(w)

#a1 = matriz([1,2,3],[2,3,4],[7,1,2])
#a2 = matriz([0,1,3],[4,0,2],[5,0,1])
#x = vector(2,5,4)

#a3 = matriz.prodvector(a1,x)
#a4 = matriz.resta(a1,a2)

#print(a3)
#print(a4)
