#Algoritmo de enumeracion exhaustiva o ataque de fuerza bruta

# También llamado “adivina y verifica” donde simplemente generamos todas las posibilidades. Técnicamente este no es un algoritmo eficiente, sin embargo, dependiendo del universo de posibilidades puede ser que sea el mas adecuado, ya que las computadoras actuales son muy rapidas y por lo tanto la eficiencia de nuestro programa no es relevante, por lo tanto siempre ten en mente este tipo de algoritmo como uno de los primeros en implementar.

# Vamos a crear un ejemplo de enumeración exhaustiva buscando la raíz cuadrada exacta de un numero

# 1.	Primero tenemos que definir cual es nuestro objetivo de raíz cuadrada. Para ello declaramos la variable objetivo que contendrá como valor el input pidiendo el int
# 2.	Generamos una variable respuesta que tendrá como ese valor inicial que será 0
# 3.	Ahora generamos una iteración sencilla con while, que tendrá la lógica de mientras la respuesta al cuadrado sea menor que el objetivo: aumentaremos la respuesta en 1
# while respuesta**2 < objetivo:
#             respuesta2 += 1
# esto es que nosotros probaremos 
# 1*1, 2*2, 3*3 (…) hasta que encontremos la raíz cuadrada del entero, que estamos buscando o nos demos cuenta que ese numero no tiene una raíz cuadrada exacta.
# 4.	Ademas, para poder dar respuesta necesitaremos una condicional con la siguiente lógica: si la respuesta al cuadrado es igual al objetivo: imprime, cadena de formato (f’La raíz cuadrada de {objetivo} es {respuesta’}, else, imprime que el objetivo no tiene una raíz cuadrada exacta.

objetivo = int(input('Escoge un entero: '))
respuesta = 0

while respuesta**2 < objetivo:
    print(respuesta) #Para saber como se ejecuta el programa
    respuesta += 1

if respuesta**2 == objetivo:
    print(f'La raiz cuadrada de {objetivo} es {respuesta}')
else:
    print(f'{objetivo} no tiene una raiz cuadrada exacta')
