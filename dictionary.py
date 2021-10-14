# Los diccionarios son como listas, pero en luar de usar índices utilizan llaves.
# No tienen orden interno. Los diccionarios son mutables. Pueden iterarse

# Los diccionarios no tienen orden interno. Es importante comprender:

# que es una función Hash? Una función hash es método para generar claves o llaves que representen de manera unívoca a un documento o conjunto de datos. Es una operación matemática que se realiza sobre este conjunto de datos de cualquier longitud, y su salida es una huella digital, de tamaño fijo e independiente de la dimensión del documento original. El contenido es ilegible.
# Es posible que existan huellas digitales iguales para objetos diferentes, porque una función hash tiene un número de bits definido. En el caso del SHA-1, tiene 160bits, y los posibles objetos a resumir no tienen un tamaño límite. A partir de un hash o huella digital, no podemos recuperar el conjunto de datos originales. Los más conocidos son el MD5 y el SHA-1, aunque actualmente no son seguros utilizarlos ya que se han encontrado colisiones. Cifrar una huella digital se conoce como firma digital.

# Requisitos que deben cumplir las funciones hash:
# Imposibilidad de obtener el texto original a partir de la huella digital.
# Imposibilidad de encontrar un conjunto de datos diferentes que tengan la misma huella digital (aunque como hemos visto anteriormente es posible que este requisito no se cumpla).
# Poder transformar un texto de longitud variable en una huella de tamaño fijo (como el SHA-1 que es de 160bits).
# Facilidad de empleo e implementación.
 

# Los diccionarios además, son mutables, e iterables a través de sus valores o sus llaves. 

# 1.	generamos un diccionario que sea llamado my_dict = { 
# ‘David’: 35,
# ‘Erika’: 32,
# ‘Jaime’: 50.
# }
# 2.	Para acceder por ejemplo a la edad de David, tenemos que llamar su llave my_dict[‘David’]
# 3.	Si queremos por ejemplo acceder a una llave que no existe, pero le podemos decir que la cree
my_dict.get(‘Juan’, 30)
# 4.	Si queremos reasignar un valor, por ejemplo volver a Jaime mas viejo y agregarle 20 anos,
my_dict[‘Jaime’] = 20
# 5.	Cuando además queremos borrar valores, podemos utilizar el keyword del. 
del my_dict[‘Jaime’]
# 6.	Si queremos iterar, podemos hacerlo a través de llaves, valores o ambas.
for llave in my_dict.keys():
       print(llave)
for valor in my_dict.keys():
       print(valor)

# for llave, valor in my_dict.keys():
#        print(llave, valor)

# 7.	Para saber si existe una llave dentro de un diccionario:
‘David’ in my_dict
True #porque la llave David, existe.






# Dictionary Comprehension es un metodo que te permite crear un nuevo diccionario apartir de un diccionario ya existente, y poder modificar las llaves y valores de acuerdo a tus necesidades, la sintaxis es:
my_dict={'Juan' : 20, 'Ana': 30, 'Arturo' : 45}

Nuevo_dict = {k:v for (k:v) in my_dict.items() if v<40}
# en donde:
# Nuevo_dict = Es el nuevo diccionario que se hara apartir de un diccionario ya existente ( my_dict)
# k:v = key : Values del nuevo diccionario ( Nuevo_dict)
# For = Loop
# (k:v) in my_dict.items() = Key : values del diccionario existente ( my_dict)
# If = Condicionante
# v = condicion (value<40)
# Dando como resultado:
# print(Nuevo_dict)
{'Juan' : 20, 'Ana': 30}
# Otro ejemplo:
my_dict={'Juan' : 20, 'Ana': 30, 'Arturo' : 45}

Estudiantes_dict = {'Estudiante ' + k:v*2 for (k:v) in my_dict.items()}
# En este caso se le agrega la palabra estudiante a todos las llaves y su valor se multiplica por 2, no hay condicionante:
print(Estudiantes_dict)
{'Estudiante Juan' : 40, 'Estudiante Ana': 60, 'Estudiante Arturo' : 90}







# Escribí este pequeño programa que te permite guardar la contraseña de tus cuentas en redes sociales:

#Para cada elemento se define la estructura clave:valor:

#Store the names of the users and the passwords
#sotre user names and passwords and ask the user to sing in
try:
	import sys
except ImportError:
	print()
	print("ERROR: Module 'sys' wasn't found")
else: 
	pass

list1 = []

def add_element_function(listt):
	"""ask for service name, username and password
		then store it in the list

		(Remember to press "Q" to quit this windows!)
	"""

	service_name = str(input("Enter web site/app name: "))
	user_name = str(input("Enter user name: "))
	user_password = str(input("Enter user password: "))

	new_item = {
		"service": service_name, 
		"user": user_name,
		"password": user_password
		}

	listt.append(new_item)
	print("Status: Element added")
	print(f"Current elements: {len(listt)}")
	print()
	return listt 

	
def list_viewer(listt):
	"""view all elements
		in a given list

		(Remember to press "Q" to quit this windows!)
	"""
	if len(listt) == 0:
		print("There are no elements")
		print()
	else:
		i = 0
		for dictionary in listt:
			i += 1
			print(f"Account #{i} »»")
			print(
				"\tService Name: ", dictionary["service"], "\n",
				"\tUser Name: ", dictionary["user"], "\n",
				"\tPassword: ", dictionary["password"], "\n",
				)

def process_info(process):
	"""Show the information of the processes
		executed in each command

		(Remember to press "Q" to quit this windows!)
	"""
	help(process)

def remove_element(listt):
	"""Prints all the registered accounts
		Asks user which one does he/she wants to remove
		Remove the account

		(Remember to press "Q" to quit this windows!)
	"""

	for dictionary in listt:
			print(
				dictionary["service"], "\n",
				dictionary["user"], "\n",
				dictionary["password"], "\n",
				)

	user_input = int(input("Which account do you wanna delete from here? (please type the position): "))
	del listt[user_input]
	print()
	return listt

menu = {
	"1": "Add new element",
	"2": "View all current elements",
	"3": "Info",
	"4": "Remove",
	"5": "Exit"
}
while(True):
	for key, value in menu.items():
		print(key +")", value)
	try:
		user_option = input()
		if user_option not in menu:
			raise TypeError
	except TypeError:
		print(f"ERROR: '{user_option}' is not a valid command, please type a valid one (1/2/3/4/5)")
	else:
		pass
		
	if user_option == "1":
		add_element_function(listt = list1)
	elif user_option == "2":
		list_viewer(listt = list1)
	elif user_option == "3":
		while(True):
			option1 = str(input("Which process do you wanna know how it works? (1/2/3/4): "))
			if option1 == "1":
				process_info(process = add_element_function)
				break
			elif option1 == "2":
				process_info(process = list_viewer)
				break
			elif option1 == "3":
				process_info(process = process_info)
				break
			elif option1 == "4":
				process_info(process = remove_element)
				break
			else:
				print(f"'{option1}' is not a command, please type a valid command (1/2/3/4): ")
				print()
	elif user_option == "4":
		remove_element(listt = list1)
	else:
		if user_option == "5":
			print("Glad I helped you!")
			sys.exit()