# Afirmaciones
# Las afirmaciones son un mecanismo en la que podemos determinar si una afirmación se cumple o no se cumple y poder seguir adelante con la ejecución de nuestro programa o darle término.
# Las afirmaciones es un método de programación defensiva, esto significa que nos estamos preparando para verificar que los tipos de inputs de nuestro programa es del tipo que nosotros esperamos. Estos también nos sirven para debuggear.
# Para realizar una afirmación en nuestro programa lo hacemos con la expresión assert <expresion booleana>, <mensaje de error>.

def primera_letra(lista_de_palabras):
    primeras_letras = []

    for palabra in lista_de_palabras:
        assert type(palabra) == str, f'{palabra} no es str'
        assert len(palabra) > 0, 'No se permiten str vacios'

        primeras_letras.append(palabra[0])

    return primeras_letras
