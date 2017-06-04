#!/usr/bin/python
# -*- coding: utf-8 -*-

#Función para calcular determinante de matriz 2x2

def determinante2x2():

	a1 = matrix[0][0]
	a2 = matrix[0][1]
	a3 = matrix[1][0]
	a4 = matrix[1][1]

	a1 = int(a1)
	a2 = int(a2)
	a3 = int(a3)
	a4 = int(a4)

	v1 = a1 * a4
	v2 = (a2 * a3)
	res = v1 - v2 

	print "El determinante es:" + str(res)

#Función para calcular determinante de matriz 3x3

def determinante3x3():

	a1 = matrix[0][0] 
	a2 = matrix[0][1] 
	a3 = matrix[0][2] 
	a4 = matrix[1][0] 
	a5 = matrix[1][1] 
	a6 = matrix[1][2] 
	a7 = matrix[2][0] 
	a8 = matrix[2][1] 
	a9 = matrix[2][2] 

	a1 =  int(a1)
	a2 =  int(a2)
	a3 =  int(a3)
	a4 =  int(a4)
	a5 =  int(a5)
	a6 =  int(a6)
	a7 =  int(a7)
	a8 =  int(a8)
	a9 =  int(a9)

	v1 = (a1 * a5 * a9) + (a2 * a6 * a7) + (a3 * a4 * a8)
	v2 = ((a7 * a5 * a3) + (a8 * a6 * a1) + (a9 * a4 * a2))

	res = v1 - v2

	print "El determinante es: " + str(res)


print "\nCALCULADORA DE MATRICES 2x2 y 3x3\n"

num = raw_input("Especifique el tamaño de su matriz, siendo cuadrada: ")
num = int(num)

#Se crea la matriz
matrix = [None] * num
for i in range(num):
   		matrix[i] = [None] * num



# Se agregan los valores an y se imprime al usuario.
if num == 2:

	matrix[0][0]= "a1"
	matrix[0][1]= "a2"
	matrix[1][0]= "a3"
	matrix[1][1]= "a4"
	
	for i in range(num):
		print matrix[i]


if num == 3:
	matrix[0][0] = "a1"
	matrix[0][1] = "a2"
	matrix[0][2] = "a3"
	matrix[1][0] = "a4"
	matrix[1][1] = "a5"
	matrix[1][2] = "a6"
	matrix[2][0] = "a7"
	matrix[2][1] = "a8"
	matrix[2][2] = "a9"

	for i in range(num):
		print matrix[i]

# Se piden los valores an, uno por uno al usuario y luego se imprime la matriz con los valores
if num == 2:
	print("\ningrese los valores de la matriz: \n")
	a1 = raw_input("\na1= ")
	a2 = raw_input("\na2= ")
	a3 = raw_input("\na3= ")
	a4 = raw_input("\na4= ")


	matrix[0][0]= a1
	matrix[0][1]= a2
	matrix[1][0]= a3
	matrix[1][1]= a4

	print("Esta es su matriz:\n")

	for i in range(num):
			print matrix[i]



if num == 3:
	print("\ningrese los valores de la matriz: \n")
	a1 = raw_input("\na1= ")
	a2 = raw_input("\na2= ")
	a3 = raw_input("\na3= ")
	a4 = raw_input("\na4= ")
	a5 = raw_input("\na5= ")
	a6 = raw_input("\na6= ")
	a7 = raw_input("\na7= ")
	a8 = raw_input("\na8= ")
	a9 = raw_input("\na9= ")

	matrix[0][0] = a1
	matrix[0][1] = a2
	matrix[0][2] = a3
	matrix[1][0] = a4
	matrix[1][1] = a5
	matrix[1][2] = a6
	matrix[2][0] = a7
	matrix[2][1] = a8
	matrix[2][2] = a9
	print("Esta es su matriz:\n")

	for i in range(num):
			print matrix[i]


#Menú de opciones

print("\n-------MENU-------")
print("1) Calcular determinante: ")

opc = input("\n:")

if opc==1 & num==2:
	determinante2x2();

elif num==3:
	determinante3x3();
