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





x = complejo(2.5,4)
y = complejo(1,5)
z = complejo.resta(x,y)
q = complejo.producto(x,y)
w = complejo.division(x,y)

print(x)
print(y)
print(z)
print(q)
print(w)