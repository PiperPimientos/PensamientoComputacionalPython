# Este es un tema MUY importante. Aun a los mejores ingenieros del mundo, les pasa que sus programas tienen una tendencia a generar bugs.

# La mejor forma de evitar bugs es con los test, asi probablemente no tendremos tantos bugs, pero seguirán sucediendo.

# Hay unas reglas generales para atacar bugs, aun cuando tenemos un test y no funciono:
# 1.	No hay que molestarse con el debugger. Aprende a utilizar el print statement. El print statement nos da una mirada a lo que esta ocurriendo dentro del programa y poder ver donde esta el error. 
# 2.	Estudia los datos disponibles
# 3.	Utiliza los datos para crear hipoteses y experimentos. Metodo científico, esto es, una vez que generamos esas pruebas en forma de test, lo importante es mantener una mente abierta y preguntarse por que un programa esta computando de esa manera, pues la computadora siempre hace lo que le decimos, no nos preguntemos en cambio, por que no esta funcionando.
# 4.	Ten una mente abierta. Si entendieras el programa, probablemente no habrían bugs.
# 5.	Lleva un registro de lo que has tratado, preferentemente en la forma de test.

# Como diseñamos los experimentos?
# Debuggear es un proceso de búsqueda. Cada prueba debe acotar el espacio de búsqueda. Una de las mejores formas de realizar esta acotación es con los print statements y utilizando Busqueda binaria. Significa que si no tenemos idea donde comienza el bug, podríamos ver, partiendo a la mitad, desde donde funciona el bug, si una parte del código funciona bien y la otra no.

#  Cuales son los errores comunes o usual suspects?

# Tenemos que encontrar los sospechos comunes, es decir, por ejemplo, pasar los argumentos en orden incorrecto, escribimos mal los nombres, no inicializamos una variable, entonces trae valor de none, comparamos dos floats con un valor exacto y no con una aproximación, comparamos un valor en vez de un objeto, utilizamos una función con efectos segundarios o por ejemplo creamos un alias sin entender por que, o hay veces que generamos un error típico de nosotros mismos.
# Es probable que el bug no este donde queremos que esta, y por eso la búsqueda binaria es importante, hay que ser sistemáticos.
# Tenemos que poder explicarle el error a otras personas.
# Es importante llevar el registro de lo que hemos hecho o hemos tratado para solucionar el bug y de preferencia este registro debe quedar en test, porque no podemos perder de vista lo que hemos intentado.
