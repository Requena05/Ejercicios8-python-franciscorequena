class Producto:
    def __init__(self,nombre,precio,codigo):
        self.nombre=nombre
        self.precio=precio
        self.codigo=codigo

    def __eq__(self, other):
        if self.codigo == other.codigo:
            return f'Los productos son iguales'
        else:
            return f'No son iguales los productos'