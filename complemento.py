#CVCE Cardoso Valencia Carlos Eric
#RHED Romero Huratado Eduardo David
#HBDG Hernandez Bravo David Gustavo

import os

def menu():
	print(' ===================================================')
	print(' ===================================================')
	print(' \n\n\tComplementos.\n\tElige una opcion:\n')
	print(' 1) Decimal a binario complemento_a1')
	print(' 2) Binario complemento_a1 a decimal')
	print(' 3) Decimal a binario complemento_a2')
	print(' 4) Binario complemento_a2 a decimal')
	print(' 5) Limpiar pantalla')
	print(' 6) Salir del menu')

	opciones = {1:decimal_comp_a1,2:comp_a1_decimal,3:decimal_comp_a2,4:comp_a2_decimal,5:limpiar,6:salir}
	opcion = input('\nOpcion: ')

	try:
		opciones[opcion]()
	except:
		print (" Esa opcion no existe. elige una opcion valida")
		menu()
	

#FUNCIONES DEL MENU
#########################################################################

def decimal_comp_a1():
	decimal = input("Numero decimal:")
	binario = decimal_binario(decimal)
	complemento_a1 = comp_a1(binario)
	print "BINARIO"
	print binario
	print "Complemento a 1"
	print complemento_a1
	menu()

	
def comp_a1_decimal():
	binario_c1 = raw_input("Binario complemento_a1:")
	binario_c1 = list(binario_c1)					#Conversiona una lista
	binario_c1 = [int(i) for i in binario_c1]		#Lista de enteros
	binario = comp_a1(binario_c1)					#Regreso al binario (intercambiar ceros por unos y unos por ceros)
	decimal = binario_decimal(binario)

	binario.reverse()
	print "BINARIO "
	print binario	
	print "DECIMAL"
	print decimal
	menu()

def decimal_comp_a2():
	return 0

def comp_a2_decimal():
	return 0

def limpiar():
	os.system('cls')

def salir():
	print " "


##########################################

#De decimal a binario
def decimal_binario(decimal):
	binario = []

	while decimal != 1:					#Mientras el cociente sea diferente de 1
		residuo = decimal%2
		binario.append(residuo)			
		decimal = (decimal-residuo)/2	#El cocientee de la division es el nuevo decimal

	binario.append(1)					#Se agrega un 1 por el metodo		
	binario.reverse()
	
	return binario

#De binario a decimal
def binario_decimal(binario):
	decimal = 0
	binario.reverse()
	#Se recorre la cadena binaria y se agrega a la variable decimal el valor 2^i
	for i in range(len(binario)):
		if binario[i] == 1:					
			decimal += 2**i

	return decimal

def comp_a1(binario):
	complemento_a1 = []
	for i in range(len(binario)):
		#Se intercambian unos por ceros y ceros por unos
		if binario[i] == 1:
			complemento_a1.append(0)	
		else:
			complemento_a1.append(1)

	return complemento_a1

#Error en este metodo
"""
def comp_a2(binario):
	complemento_a2 = [None]*len(binario)
	binario.reverse()
	cta = 0
	for i in range(len(binario)):
		if binario[i] != 1:
			complemento_a2[i] = binario[i]
		
		else: 
			if cta != 0:
				complemento_a2[i] = binario[i]
				cta+=1
			else:
				if binario[i] == 1:
					complemento_a2[i] == 0
				else:
					complemento_a2[i] == 1


	complemento_a2.reverse()
	return complemento_a2

"""
menu()