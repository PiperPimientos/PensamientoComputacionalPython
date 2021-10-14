#Funciones como objetos

# Una de las características más poderosas de Python es que todo es un objeto, incluyendo las funciones. Las funciones en Python son “ciudadanos de primera clase”.

# Esto, en sentido amplio, significa que en Python las funciones:

# Tienen un tipo
# Se pueden pasar como argumentos de otras funciones
# Se pueden utilizar en expresiones
# Se pueden incluir en varias estructuras de datos (como listas, tuplas,
# diccionarios, etc.)




# ARGUMENTOS DE OTRAS FUNCIONES
# Hasta ahora hemos visto que las funciones pueden recibir parámetros para realizar los cómputos que definen. Algunos de los tipos que hemos pasado son tipos simples como cadenas, números, listas, etc. Sin embargo, también pueden recibir funciones para crear abstracciones más poderosas. Veamos un ejemplo:

def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(f, numeros):
    resultados = []
    for numero in numeros:
        resultado = f(numero)
        resultados.append(resultado)
        return resultados

# >>> nums = [1, 2, 3]
# >>> aplicar_operacion(multiplicar_por_dos, nums)
# [2, 4, 6]

# >>> aplicar_operacion(sumar_dos, nums)
# [3, 4, 5]

# me costaba entender esto al principio porque prácticamente sale de la nada. En este caso, operacion es un iterador de la lista operaciones que con cada ciclo va tomando las operaciones contenidas en dicha lista una por una y aplicándolas al parámetro num. Como la lista operaciones tiene 2 elementos, el ciclo for se ejecutará 2 veces, pasando por cada elemento.
# Paso a paso:
# def aplicar_operaciones(num):
# Definimos una nueva función aplicar_operaciones que recibe como parámetro num.
# 	operaciones = [abs, float]
# Se crea una nueva lista llamada operaciones que contiene 2 elementos: la función integrada abs() y la función integrada float().
# 	resultado = []
# Se crea una nueva lista vacía llamada resultado que usaremos más adelante
# 	for operacion in operaciones:
# Creamos el iterador operacion y recorremos todos los elementos de la lista llamada operaciones uno por uno. Por cada operacion (elemento dentro de la lista operaciones), se ejecuta el código debajo
# 		resultado.append(operacion(num))
# A la lista vacía resultado le vamos a agregar (append) el resultado de operar el parámetro num con la operacion (elemento) seleccionada actualmente.
# EJEMPLO: Supongamos que es la primera vez que se ejecuta el ciclo. El primer elemento usado (operacion) sería abs. Entonces, se realizará la operación abs(num).
# 	return resultado
# Una vez terminado todo el ciclo for, devuelve el resultado.

# Como pudimos ver, las funciones son objetos muy versátiles que nos permiten tratarlas de diversas maneras y que nos permiten añadir capas adicionales de abstracción a nuestro programa.
# Compártenos cómo te imaginas que estas capacidades de Python te pueden ayudar a escribir mejores programas.







# FUNCIONES EN EXPRESIONES
# Una forma de definir una función en una expresión es utilizando el keyword lambda. lambda tiene la siguiente sintaxis: lambda <vars>: <expresion>.

# Otro ejemplo interesante es que las funciones se pueden utilizar en una expresión directamente. Esto es posible ya que como lo hemos platicado con anterioridad, en Python las variables son simplemente nombres que apuntan a un objeto (en este caso a una función). Por ejemplo:

sumar = lambda x, y: x + y

resultados = sumar(int(input('ingrese primer valor:')),int(input('ingrese segundo valor:')))
print(resultados)

# >>> sumar(2, 3)
# 5





# FUNCIONES EN ESTRUCTURAS DE DATOS
# Las funciones también se pueden incluir en diversas estructuras que las permiten almacenar. Por ejemplo, una lista puede guardar diversas funciones a aplicar o un diccionario las puede almacenar como valores.

def aplicar_operaciones(num):
    operaciones = [abs, float]

    resultado = []
    for operacion in operaciones:
        resultado.append(operacion(num))

    return resultado

# >>> aplicar_operaciones(-2)
# [2, -2.0]



# Como pudimos ver, las funciones son objetos muy versátiles que nos permiten tratarlas de diversas maneras y que nos permiten añadir capas adicionales de abstracción a nuestro programa.

# Compártenos cómo te imaginas que estas capacidades de Python te pueden ayudar a escribir mejores programas.