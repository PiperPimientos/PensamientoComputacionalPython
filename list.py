# Las listas son estructuras de objetos y que además son mutables.

# Las listas son secuencias de objetos, pero a diferencia de las tuplas, si son mutables

# Cuando modificas una lista, pueden existir efectos secundarios(side effects)

# Es posible iterar con ellas si utilizamos por ejemplo el for loop, con el operador de for i in list:


# Cuando queremos modificar una lista podemos:
# -	Asignar via índice (my_lista[0] = 5)
# -	Utilizar los métodos de la lista (append, pop, remove, insert, etc.)

# En las listas podemos asignar y llamar un elemento de la lista con el índice, asi:

my_list = [1, 2, 3]

my_list[0]


# E incluso utilizar slices para crear listas nuevas.
my_list[1:0]
[2, 3]

# Y de ahí en adelante: utilizar los métodos que modifican (append, pop, remove, insert, etc.), generar iteraciones con el for loop, e incluso muchos otros métodos que encontramos.

# Si vemos una de esos side effects de las modificaciones, aquí hay un ejemplo:

# 1.	Creamos dos listas, la a y la b, la a tiene como valores el 1, 2 y 3. La b, tiene a como valor. Aquí lo que pasa es que ambas están apuntando al mismo lugar en memoria, pero no es que se hayan reasignado. Es decir que tienen el mismo lugar en memoria:

 


# Aquí es donde podemos tener errores, porque si quisiéramos por ejemplo generar una lista de listas, como c = [a, b]. Y si luego llamo por ejemplo la lista a para modificarla, se modificarían las otras listas.

 

# Es uno de los errores mas comunes en programación, sobretodo cuando andamos de función en función o lista en lista, y cada una modifica la anterior.

# Esta prohibido de hecho, en patrones del desarrollo web, que nos prohíben generar datos mutables, que nos obligan a generar copias, para ello veremos la clonación.

# Clonación:

# Una forma de evitar los side effects es clonar la lista, casi siempre es mejor clonar una lista en vez de mutarla. Para clonar una lista podemos utilizar slices que clonan una lista de una en una, o la función list

# 1.	Generaremos una lista que se llame igual que la teníamos antes a = [1, 2, 3]. Y si vemos el id, nos daremos cuenta que no es el mismo objeto.
# 2.	Luego vamos otra vez a asignar b = a y veremos que efectivamente tiene el mismo id.
# 3.	Ahora con c en vez de asignarlas directamente, utilizaremos la función list(a). Y cuando comparamos ambos id, tenemos diferentes objetos.
# 4.	O podemos también clonarlo con una anotación de slices, que diga, empieza en el principio, termina en el final d = a[::] vete de 1 en 1. 

# List comprehension

# Es otro tema importante de las listas.
# Es una forma concisa de aplicar operaciones a los valores de una secuencia
# También se pueden aplicar condiciones para filtrar.

# 1.	Generaremos una lista de un rango my_list = list(range(100)). Si ejecutamos veremos que nos genera una lista del 0 al 99
# 2.	Si queremos doblar esa lista, decimos por ejemplo que
# double = [ ] 
# y aquí adentro viene nuestro list comprehension donde lo inicializamos directamente, y colocaremos lo siguiente
# a.	La expresion de multiplicado por dos que es i * 2
# b.	for loop, que tenga la lógica que  for i in my_list
# 3.	Si quisiéramos sacar solo los valores pares, 
pares = [i for i in my_list if i % 2 == 0] 
# Con la logica de que si yo lo divido por 2 y es igual a 0 el modulo, entonces es par.

# Acá investigue los métodos de listas: https://docs.python.org/3/tutorial/datastructures.html#more-on-lists
# Los nuevos que encontré además de los de la clase:
# •	lista.extend(iterable) #extiende la lista con valores dentro de un iterable como un range()
# •	lista.insert(i, ‘valor’) #Agrega un valor en la posición i y recorre todos los demás. No borra nada.
# •	lista.pop(i) #Elimina valor en la posición i de la lista.
# •	lista.remove(‘valor’) #Elimina el primer elemento con ese valor.
# •	lista.clear() #Borra elementos en la lista.
# •	lista.index(‘valor’) #Retorna posición del primer elemento con el valor.
# •	lista.index(‘valor’, start, end) #Retorna posición del elemento con el valor dentro de los elementos desde posición start hasta posición end)
# •	lista.count(‘valor’) #Cuenta cuántas veces esta ese valor en la lista.
# •	lista.sort() #Ordena los elementos de mayor a menor.
# •	lista.sort(reverse = True) #Ordena los elementos de menor a mayor.
# •	lista.reverse() #Invierte los elementos
# •	lista.copy() #Genera una copia 
