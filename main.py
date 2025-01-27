from Calculadora import Calculadora
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


































'''6. Intersección y Diferencia de Conjuntos
Crea dos conjuntos registrados y aprobados. Usa intersección para obtener los
alumnos que están en ambas listas y diferencia para los registrados que no
aprobaron.
Muestra ambos resultados.'''

registrados=["Fran","Manu","Nacho","Jaime"]
aprobados=["Manu","Nacho"]

print("Alumnos aprobados: ",list(set(registrados).intersection(set(aprobados))))
print("Alumnos suspendidos: ",list(set(registrados).difference(set(aprobados))))


'''7. Clase con Métodos Estáticos
Crea una clase Calculadora con métodos estáticos para sumar, restar,
multiplicar y dividir.
Llama a los métodos directamente desde la clase sin crear un objeto.'''



print(Calculadora.multiplicar(122421412421421414214124124123465433451437663475487658622222,212222222232324213124133124214214124214214))


'''8. Diccionario con Métodos
Implementa una clase Agenda con un diccionario para almacenar contactos
(nombre: teléfono). Crea métodos para agregar, eliminar y buscar contactos.
Agrega varios contactos, búscalos y elimínalos.'''

miscontactos={}



