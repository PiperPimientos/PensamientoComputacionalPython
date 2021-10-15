# La diferencia entre las pruebas de Caja Negra y Caja de Cristal es que en las pruebas de caja negra se escriben primero los test para ayudarnos a implementar nuevo código. En las pruebas de caja de cristal se asume que se tiene código escrito y las pruebas se escriben para verificar todas las ramificaciones del programa y probar todos los diferentes caminos posibles.
# Las pruebas de caja de cristal se basan en el flujo del programa. Prueba todos los caminos posibles de una función. Ramificaciones, bucles for y while, recursión. 
# Estas pruebas son muy buenas cuando tenemos que hacer regression testing, es decir que descubrimos el bug cuando el programa ya salió a luz y entonces tenemos que determinar donde esta ese bug. Y ahí, para poderlo determinar tenemos que saber como esta estructurado el código.
# Como funcionan las ramificaciones:

# 1.	Si nosotros tenemos un if, tenemos que probar todas las condiciones.
# 2.	Si nosotros tenemos un loop y queremos probar una test donde entremos 1, 2 o mas veces al loop
# 3.	Si tenemos un while loop queremos tener una prueba donde la condición de entrada sea falsa y una prueba donde veamos los break statements y por ultimo es importante probar todas las excepciones que pueda tener nuestro código, es decir, todos los lugares en donde puedan haber errores.
# Crearemos nuestro código para ver como es 

# 1.	Crearemos la misma estructura de la caja negra, desde importar el modulo unittest, luego creando la Clase PruebaDeCristalTest que extienda (unittest.TestCase):
# 2.	inicializamos el modulo con nuestro if __name__ == ‘__main__’: entonces vamos a correr nuestra función main dentro del modulo unittest
# unittest.main()

# import unittest

# class PruebaDeCristalTest(unittest.TestCase):
#     pass

# if __name__ == '_main_':
#     unittest.main()

# 3.	En la caja de cristal se asume que ya el código esta escrito, por lo que no escribiremos los test previamente al código.
# 4.	Asi que comenzamos con una función, def es_mayor_de_edad(edad) que recibe como parámetro la edad
# 5.	y le asignamos como condición que si la edad es mayor o igual a 18 years. return True
# else: return False.
# 6.	Tuvimos que escribir ambas condiciones con el return, para saber si es false o true, que es mayor de edad
# 7.	Ahora tendremos que generar dos test, uno par cada camino. Asi que nos vamos a nuestra class, crearemos una reasignación para edad, que sea de 20, y una variable resultado que tenga asignada la función es_mayor_de_edad(edad), y por ultimo, verificamos que el resultado sea igual a True, para que represente ese camino de True.
# 8.	Si lo ejecutamos, veremos que al correr nuestro primer test nos dice que es OK
# 9.	Ahora escribimos nuestro segundo test que será  si es menor de edad
# 10.	 Ejecutamos y vemos que esta OK
# 11.	Ahora si vamos a nuestra función es_mayor_de_edad y cambiamos booleano del if, por un False, accidentalmente. Si nosotros volvemos a cambiar nuestra suit de test, nos daremos cuenta que tenemos un error.



import unittest

def es_mayor_de_edad(edad):
    if edad >= 18:
        return True
    else:
        return False

class PruebaDeCristalTest(unittest.TestCase):
    

    def test_es_mayor_de_edad(self):
        edad = 20

        resultado = es_mayor_de_edad(edad)
        
        self.assertEqual(resultado, True)

    def test_es_menor_de_edad(self):
        edad = 15

        resultado = es_mayor_de_edad(edad)
        
        self.assertEqual(resultado, False)



if __name__ == '_main_':
    unittest.main()



# Aporte que me gusto:

# El testing tambien es un campo interesante,
# Aqui la lista de los ** 7 principios de Testing ** de acuerdo al libro de ISTQB.
# 1 Las pruebas muestran la presencia de defectos
# Significa que las pruebas pueden demostrar que EXISTEN problemas, pero no que los problemas NO EXISTEN.
# El objetivo principal de llevar a cabo una prueba es para detectar defectos. Trabajando bajo la premisa de que cada producto contiene defectos de algún tipo, una prueba que revela los errores es generalmente mejor que una que no lo hace. Todas las pruebas por lo tanto, deben ser diseñados para revelar tantos errores como sea posible
# 2 Las pruebas exhaustivas son imposibles
# Las pruebas exhaustivas tratan de cubrir todas las combinaciones posibles de datos en el software, a fin de garantizar que ninguna situación puede surgir, una vez probado el software se ha liberado. Excepto en aplicaciones muy simples, el número de combinaciones posibles de datos es demasiado alta, es más eficaz y eficiente que los ingenieros de pruebas se centren en las funcionalidades de acuerdo a riesgos y prioridades.
# 3 Pruebas tempranas.
# Un producto (incluyendo los documentos, tales como la especificación del producto) se puede probar tan pronto como se ha creado. ISTQB recomienda probar un producto tan pronto como sea posible, corregir los errores más rápidamente posible. Los estudios han demostrado que los errores identificados al final del proceso de desarrollo por lo general cuestan más para resolver.
# Por ejemplo: un error encontrado en las especificaciones puede ser bastante sencillo de solucionar. Sin embargo, si ese error se transfiere a la codificación de software, una vez descubierto el error puede ser muy costoso y consume tiempo.
# 4 Agrupamiento de Defectos
# Los estudios sugieren que los problemas en un elemento de software tienden a agruparse en torno a un conjunto limitado de módulos o áreas. Una vez que estas áreas han sido identificadas, los administradores eficientes de prueba son capaces de enfocar las pruebas en las zonas sensibles, mientras que siguen buscando a los errores en los módulos de software restantes. Me recuerda al 80/20.
# 5 La paradoja del “Pesticida”
# Al igual que el sobre uso de un pesticida, un conjunto de pruebas que se utilizan repetidamente en el disminuirá en su eficacia. Usando una variedad de pruebas y técnicas expondrá una serie de defectos a través de las diferentes áreas del producto.
# 6 La prueba es dependiente del contexto
# Las mismas pruebas no se deben aplicar en todos los ámbitos. Distintos productos de software tienen diferentes requisitos, funciones y propósitos. Una prueba diseñada para realizarse en un sitio web, por ejemplo, puede ser menos eficaz cuando se aplica a una aplicación de intranet. Una prueba diseñada para una forma de pago con tarjeta de crédito puede ser innecesariamente rigurosa si se realiza en un foro de discusión.
# En general, cuanto mayor es la probabilidad y el impacto de los daños causados por el software fallado, mayor es la inversión en la realización de pruebas de software.
# 7 La falacia de ausencia de errores
# Declarar que una prueba no ha descubierto ningún error no es lo mismo que declarar que el software es “libre de errores”. Con el fin de garantizar que los procedimientos adecuados de software de prueba se lleva a cabo en todas las situaciones, los evaluadores deben asumir que todo el software contiene algunos (aunque disimulada) errores.
