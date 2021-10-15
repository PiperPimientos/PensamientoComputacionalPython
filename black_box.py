# Estas son una serie de técnicas para atacar los bugs de manera directa. El primer tipo son las pruebas de caja negra.

# Las pruebas de caja negra se basan en la especificación de la función o el programa, aquí debemos probas sus inputs y validar los outputs. Se llama caja negra por que no necesitamos saber necesariamente los procesos internos del programa, solo contrastar sus resultados.
# Estos tipos de pruebas son muy importantes para 2 tipos de test:
# •	Unit testing: se realizan pruebas a cada uno de los módulos para determinar su correcto funcionamiento.
# •	Integration testing: es cuando vemos que todos los módulos funcionan entre sí.
# Es una buena práctica realizar los test antes de crear tus lineas de código, esto es por que cualquier cambio que se realice a futuro los test estaran incorporados para determinar si los cambios cumplen lo esperado.
# En Python existe la posibilidad de realizar test gracias a la libreria unittest. Puede ser que el siguiente código no lo entiendas en su totalidad, pero en una próxima guía detallare mas el tema de clases en programación. Por ahora te mostrare como se realizan estos test.


# """Importamos la libreria de unittest."""
import unittest

# """Creamos una clase para los test, en este caso se llamara
# CajaNegraTest, y como parámetro."""
class CajaNegraTest(unittest.TestCase):
#     """Definimos la funcion que generara el test."""
    def test_suma_dos_positivos(self):
       #Para nuestro ejemplo usaremos 2 parametros.
        num_1 = 10
        num_2 = 5        
        """Y dentro de la variable resultado
        guardaremos lo que nos retornara la función suma."""
        resultado = suma(num_1, num_2)        
        """Y para terminar definimos la variable resultado
        y cual es el valor esperado."""
        self.assertEqual(resultado, 15)


# """Para definir el módulo de Python escribimos lo siguiente."""
if __name__ == '__main__':
    unittest.main()
# Luego de escribir nuestro archivo iremos a la consola y ejecutaremos el test
# python3 caja_negra.py

# Obtenemos un error en nuestro test
# ======================================================================
# ERROR: test_suma_dos_positivos (__main__.CajaNegraTest) # Veremos aqui el test con error
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "caja_negra.py", line 9, in test_suma_dos_positivos
#     resultado = suma(num_1, num_2)
# NameError: name 'suma' is not defined   # La función suma no esta definida

# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# FAILED (errors=1)

# Como vimos en el recuadro anterior no definimos la función suma, para ello vamos a crearla.
import unittest

def suma(num_1, num_2):
    return num_1 + num_2

class CajaNegraTest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5
        resultado = suma(num_1, num_2)
        self.assertEqual(resultado, 15)

if __name__ == '__main__':
   unittest.main()
# Ahora ejecutaremos denuevo nuestro test en la terminal.
# python3 caja_negra.py
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.000s

# OK


# Ya tenemos nuestro primer test funcionando. Una vez que ya tenemos un test funcionando y seguimos agregando test, tenemos una garantía que si un dia cambiamos esta función y el código deja de funcionar como queríamos, nuestra suit de test nos va decir de inmediato que hay un componente en el código que ya no funciona.

# Si agregamos otro test, que sea para sumar dos negativamos por ejemplo
# 1.
	def test_suma_dos_negativos(self):
        num_1 = 10
        num_2 = -7

    resultado = suma(num_1, num_2)
    self.assertEqual(resultado, -17)



# Si ejecutamos el código, vemos que ya tenemos un segundo test que funciona


# 2.	Imaginemos que algún dia nos despertamos y decidimos que ahora queremos que el num_1 sea un valor abs.
# 3.	Volvemos a ejecutar el código y nos dice: se ejecutaron dos test, uno si paso, pero el otro fallo, pues al cambiar el num_1 por un abs, ya no retornaría un negativo, retornaría 3.
