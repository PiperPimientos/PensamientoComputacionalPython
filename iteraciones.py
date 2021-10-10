# Ya sabemos cómo generar programas ramificados. Las iteraciones, por otro lado, nos van a permitir realizar la misma tarea en varias ocasiones, no tenemos que escribir 10 prints si queremos imprimir del 1 al 10. Tambien se pueden escribir iteraciones dentro de iteraciones y funciona como reloj, segundos dentro de minutos, minutos dentro de horas.

# While loop: Es la primera iteración que veremos 

# Sintaxis:
# while <condicion>:
# <expresion>
# repite la expresion mientras la condicion sea verdadera
# Loop anidado
# while <condicion>:
#         while <condicion>:
#                 <expresion2>
# <expresion1>

# Ejecutamos la expresion2 un numero determinado de veces cada vez que se ejecuta la expresion1. Podemos usar un reloj como analogia a este codigo la expresion 2 como segundos y la expresion1 como minutos

# Ejemplo:

# 1.	Generaremos una variable contador que tendrá un valor asignado de 0, que es desde donde nuestro contador partira contando.
# 2.	Luego generamos la condición loop while contador < 10: vamos a imprimir el contador
# print(contador)
# 3.	La forma de ir incrementando el contador es indicarle que aumente de 1 en 1 el valor de contador con cualquiera de estas sintaxis: contador = contador + 1 o también, contador += 1

contador = 0
while contador < 10:
    print(contador)
    contador += 1 # contador = contador + 1

# Si queremos incluir un contador interno, es decir una iteración interna

# 1.	tendremos que generar dos variables una para contador_externo y otra para contador_interno, que seran asignadas a un valor de 0.
# 2.	Luego 
# while contador_externo < 5:
#           while contador_interno < 6: Vamos a imprimir ambos contadores
#                            print(contador_externo, contador_interno) Y para no tener un loop infinito debemos aumentar el contador interno de 1 en 1
#                            contador_interno += 1
#            contador_externo += 1
#            contador_intero = 0 lo ponemos en 0 otra vez, es decir, volverlo a resetear porque o sino, nunca volvería a entrar, pues ya seria mayor que 6
# 3.	Lo que pasa con este programa finalmente es que funciona como un reloj que repite un ciclo antes del valor de 6

contador_externo = 0
contador_interno = 0


while contador_externo < 5:
    while contador_interno < 6: 
        print(contador_externo, contador_interno) 
        contador_interno += 1

        if contador_interno >= 3:
            break

    contador_externo += 1
    contador_interno = 0

# Infinite loop: sucede cuando la condicion siempre es verdadera, el programa nunca termina
# •	Si eliminamos: contador_interno += 1 se genera un infinite loop, ya que siempre sería verdad (al inicio dicho contador se le asignó cero)
# •	Si eliminamos: contador_externo += 1 también se genera un infinite loop, como al inicio se asigno el valor de cero, siempre será verdad.
# •	Si eliminamos: contador_interno = 0 ocurre solo una iteracion, pues como queda asigando el valor de 6 al contador_interno el segundo while va ser falso siempre. (no hay un infinite loop)




#Ejercicio: Creacion de un reloj de 24hrs

hora, minu, seg = 0, 0, 0
while hora < 24:
    while minu < 60:
        while seg < 60:
            print(hora, minu, seg)
            seg += 1
        
        minu += 1
        seg = 0
    
    hora += 1
    minu = 0

#Ejercicio 2: Creacion de un loop con forma de rombo

def run():
    maximo = int(input('Introduzca un numero entero para definir el tamano de su rombo: '))

    i = maximo

    counter = 0

    while i > 0:
        impresion = '*' * i
        print(impresion + ' ' + counter + impresion)
        i -+ 1
        counter += 2
    
    counter -= 2
    i = 1

    while i < maximo + 1:
        impresion = '*' * i
        print(impresion + ' ' * counter + impresion)
        i += 1
        counter -= 2
