# Las excepciones son cuando sucede un error en el código y son bastante comunes. No tienen nada de excepcional.
# Las excepciones de Python normalmente se relacionan con errores de semántica. 
# Se pueden crear excepciones propias.
# Excepciones comunes:
# ImportError : una importación falla;
# IndexError : una lista se indexa con un número fuera de rango;
# NameError : se usa una variable desconocida ;
# SyntaxError : el código no se puede analizar correctamente
# TypeError : se llama a una función en un valor de un tipo inapropiado;
# ValueError : se llama a una función en un valor del tipo correcto, pero con un valor inapropiado


# Manejo de excepciones
# Se manejan con 3 keywords que son try, except, finally. En JavaScript es el try catch, por ejemplo.
# Las excepciones no solo sirven para los errores, se pueden utilizar también para ramificar programas. Por ejemplo podemos intentar algo, si esto no funciona y nos tira una excepción, directamente en el manejo de la excepción podemos continuar con el programa.
# No deben manejarse de manera silenciosa(por ejemplo, con print statement). Esto significa que utilizamos el try y el except y en lugar de manejar el error, simplemente lo imprimimos en la consola.
# Para aventar tu propia excepcion hay que utilizar el keywor raise. Esto significa que alguien que utilice nuestra función, tendrá que usar esa excepción.

# Vamos al código.
# 1.	Creamos una función que dividirá todos los elementos de lista divido entre dos.
# 2.	La función recibirá como parámetros una lista y un divisor
# def divide_elementos_de_lista(lista, divisor):
# La implementación mas sencilla es que podemos decir en un list comprehensions, que tome el índice entre el divisor por cada uno de los elementos en la lista y ahí estamos generando todas las divisiones dde una vez
# return [i / divisor for I in lista]
# 3.	Generamos la lista y el divisor
# lista = list(range(10))
# divisor = 2
# 4.	Si queremos ver que es lo que sucede
# print(divide_elementos_de_lista(lista, divisor))


# Si ejecutamos el código tendremos una division de cada elemento
 

# Hasta aquí nuestro código parece correcto, pero si le decimos que el divisor es 0, el programa no funcionara y nos tirara una excepción llamada, ZeroDivisionError:


# Para trabajar con el código, podemos agregar el Try Catch fuera de la función, es decir si somos solo usuarios de la función, o ponerlo dentro de la función y hacer un poco de programación defensiva, para hacer esto ultimo haremos lo siguiente.
# 1.	introducimos el try: dentro de la función, luego dentro del try identamos nuestro return que contiene la operación en la lista.
# 2.	Despues de cerrar lo que esta dentro de try, sigue la línea except y en el except introducimos el error que sabemos que tenemos que es ZeroDivisionError y podemos agarrar una referencia de ese error utilizando as e: 
# Dentro de su identacion, retornamos lista.


# def divide_elementos_de_lista(lista, divisor):
#     try:
#         return [i / divisor for i in lista]
#     except ZeroDivisionError as e: #esta letra e es importante por el mensaje del codigo y de ahi imprimimos el mensaje (e)rror
#         print(e)
#         return lista

# lista = list(rane(10))
# divisor = 2

# print(divide_elementos_de_lista(lista, divisor))

# # En conclusión: tenemos dos nuevos keywords, try y except que nos aseguran que no tendremos errores dentro de nuestro código y nos permite manejar estas excepciones para que nuestro código no falle cuando nos encontremos con un error.

# Excepciones como control de flujo
# Hasta ahora hemos visto como las excepciones nos permiten controlar los posibles errores que pueden ocurrir en nuestro código. Sin embargo, dentro de la comunidad de Python tienen otro uso: control de flujo.
# En este momento ya debes estar familiarizado con las estructuras de control flujo que ofrece Python (if... elif...else); entonces, ¿por qué es necesaria otra modalidad para controlar el flujo? Una razón muy específica: el principio EAFP (easier to ask for forgiveness than permission, es más fácil pedir perdón que permiso, por sus siglas en inglés).
# El principio EAFP es un estilo de programación común en Python en el cual se asumen llaves, índices o atributos válidos y se captura la excepción si la suposición resulta ser falsa. Es importante resaltar que otros lenguajes de programación favorecen el principio LBYL (look before you leap, revisa antes de saltar) en el cual el código verifica de manera explícita las precondiciones antes de realizar llamadas.
# Veamos ambos estilos:
# # Python

def busca_pais(paises, pais):
    '''
    Paises es un diccionario. Pais es la llave.
    Codigo con el principio EAFP.
    '''
    
    try:
        return paises[pais]
    except KeyError:
        return None

# // Javascript

# /**
# * Paises es un objeto. Pais es la llave.
# * Codigo con el principio LBYL.
# */
# function buscaPais(paises, pais) {
#   if(!Object.keys(paises).includes(pais)) {
#     return null;
#   }

#   return paises[pais];
# }
# Como puedes ver, el código de Python accede directamente a la llave y únicamente si dicho acceso falla, entonces se captura la excepción y se provee el código necesario. En el caso de JavaScript, se verifica primero que la llave exista en el objeto y únicamente con posterioridad se accede.
# Es importante resaltar que ambos estilos pueden utilizarse en Python, pero el estilo EAFP es mucho más "pythonico".
 
