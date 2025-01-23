from Producto import Producto
'''Ejercicio 1: Comparación de Productos
Crea una clase Producto que represente un artículo en una tienda. Esta clase
debe tener los atributos nombre, precio y codigo. Sobrecarga el método
__eq__ para considerar dos productos iguales si tienen el mismo código.'''

producto1 = Producto("Pepino","3,13","2")
producto2= Producto("Manzana","12,3","2")

print(producto1.__eq__(producto2))


'''Ejercicio 2: Biblioteca de Libros
Crea una clase Libro que tenga los atributos título, autor y isbn. Sobrecarga
los métodos __str__ y __eq__ para que los libros se puedan comparar por isbn
y mostrar una representación legible.'''

