class Vector:
    def __init__(self, x, y, z):
        self.x = x
        self.y  = y
        self.z = z

    def sumar(vector1, vector2):
        salida=Vector(vector1.x+vector2.x, vector1.y+vector2.y,vector1.z+vector2.z)
        return(salida)

    def restar(vector1, vector2):
        return(Vector(vector1.x-vector2.x, vector1.y-vector2.y,vector1.z-vector2.z)        )

    def multiplicar(vector1, vector2):
        x = (vector1.y * vector2.z) - ( vector2.y * vector1.z)
        y = (vector1.x * vector2.z) - ( vector2.x * vector1.z)
        z = (vector1.x * vector2.y) - ( vector2.x * vector1.y)
        return(Vector(x,-y, z))

    def dividir(vector, escalar):
        x = (vector.x / escalar)
        y = (vector.y / escalar)
        z = (vector.z / escalar)
        return(Vector(x, y, z))