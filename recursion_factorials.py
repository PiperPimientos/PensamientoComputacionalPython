#Recursion o recursividad, o funciones recursivas, en python, con un ejemplo de Factoriales

# La recursividad se puede definir de manera algorítmica como una forma de crear soluciones utilizando el principio de divide y vencerás, significa que un problema podemos resolverlo utilizando versiones más pequeñas del mismo problema. Es decir, un problema que al principio parecería difícil, se puede encontrar una solución base para construir iterativamente la solución final a este problema.

# Y de manera programática como una técnica programática mediante la cual una función se llama a si misma. 

# Como implementamos recursividad en código? Pues haciendo que una función dentro de su ejecución, se llame a si misma otra vez.

# Para empezar a entender la recursividad vamos a ver un primer problema que son los factoriales.

# Lo que vemos más notable es el símbolo de producto, que es una iteración, es como un for loop. Asi que lo que nos dice el ejercicio es que una n! (el signo de admiración significa factorial) es un loop que empieza en 1 (i = 1) y termina en n. Asi que si queremos el factorial de 10 y tenemos que si i empieza en 1 y termina en 10. Y finalmente, para poder llegar a 10, esta el símbolo i al lado de el símbolo de producto, que nos dice que multiplicaremos por el mismo valor hasta llegar a n, es decir que multiplicaríamos 1 por si mismo hasta llegar a 10.


# Tanto en la programación como en las matemáticas nosotros podemos definir una función recursiva tanto en un loop como en la propia recursividad. La forma factorial de definir la recursividad seria en programación:

# n! = n * ( n – 1)!	

# Y una recursión al final del dia seria simplemente una forma de iterar y cualquier función recursiva, podemos representarla como un loop.

# Si nosotros queremos obtener 4 factorial
# 4! = 4 * (4 – 1)!
# 4! = 4 * (3)! #y que es 3 factorial?
# 3! = 3 * (2)! #y que es 2 factorial?
# 2! = 2 * (1)!
# 1! = 1

# Y ahora, ese 1 lo multiplicamos por 2, lo que nos de lo multiplicamos por 3 y luego lo que nos de, lo multiplicamos por 4, y entonces estamos llegando a la solución de que

# 4! = 4*3*2*1

# Ahora un ejemplo en codigo


# 1.	Crearemos una función que se llama def factorial(n): 
# 2.	Ahora escribiremos nuestro docstring, que como buenas practicas siempre hay que escribirlo porque nos hará pensar en lo que escribiremos.
#       Nuestra especificación será:
#       Descripcion: Calcula el factorial de n
#       definimos: n es un entero que es mayor que 0
#       regresa n factorial
# 3.	Ahora que tenemos nuestro docstring, escribiremos nuestro caso base, es decir hasta donde iremos en esta iteración. En la forma en la que esta construido Python no nos generaría un infinite loop, pero si nos generaría un error porque llegamos al limite máximo de recursividad.
#        Asi que si queremos escribir n! nuestro caso base es que si n es igual a 1 entonces regresa 1. 
#        if n == 1:
#        return 1

# nota: para conocer el limite máximo de recursividad hay que importar la librería sys. print(sys.getrecursionlimit()) 1000

# 4.	Ahora si, lo que tenemos que hacer es regresar nuestra definición matemática regresa n factorial por el factorial de n menos 1
#       return n * factorial(n – 1)
      
#       Con esto ya tenemos nuestra primera funcion recursiva. Y la lógica de lo que va pasar es que si recibimos por ejemplo 3, como parámetro n, entonces si 3 no es igual a 1, no se ejecuta esa primera condicional, y luego retornara el resultado de 3 * 3(3 – 1) y luego regresa a la función y repite.
      
#       Aquí es importante tener en cuenta el concepto de los stacks, porque cada vez que la función se ejecuta, se va poniendo un stack nuevo encima.

# 5.	Ahora declararemos la variable n y le ordenaremos al usuario que nos diga un numero entero, y simplemente imprimiremos cual es la factorial de n
#       n = int(input(‘Escribe un entero: ‘))
#       print(factorial(n))

def factorial(n):
    """Calcula el factorial de n

    n int > 0
    returns n!
    """
    print(n) #Print statement para saber cual es el valor de n en cada iteracion
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

n = int(input('Escribe un entero: '))
print(factorial(n))

# Como reto hay que investigar como se implementa la recursividad en python

