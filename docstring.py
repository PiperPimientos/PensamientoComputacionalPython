# El docstring o la documentación está dividido en tres partes importantes que son las siguientes:
# •	Primero se da una descripción clara y concisa de la función y su funcionamiento
# •	En medio se agrega la descripción de los diferentes parámetros, su tipo, su nombre y que es lo que se espera de esos parámetros
# •	Por ultimo se agrega que es lo que devuelve nuestra función

# La convención en Python es utilizar la triple doble comilla para generar ese string que tenga varias líneas “ “ “ 

# Aquí vemos como podemos leer este bloque de código, donde el docstring nos indica  para que sirven los parámetros y el return y la función en si misma

# Vamos a ver como funciona el docstring con un ejemplo:

# 1.	Declaramos función def a(cualquier_parametro):
# 2.	En la identacion de la función abrimos triple doble comilla y damos la descripción, describimos cualquier_parametro, decimos si es de tipo int cualquier entero, en otra línea decimos que returns cualquier_parametro + 5 cerramos la triple doble comilla
# 3.	Ahora escribimos nuestro código tal como lo descrito y listo

def a (cualquier_parametro):
    """ Descripcion de lo que hace nuestra funcion
        cualquier_parametro int cualquier entero
        returns cualquier_parametro + 5
    """
    return cualquier_parametro

# Si queremos saber que contiene el docstring, en la consola ejecutando el programa escribimos help() y adentro, el nombre de la función, cuando hacemos esto, nos sale el docstring

help(a)

