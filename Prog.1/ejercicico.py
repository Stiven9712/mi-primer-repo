#ejercio1

#clasificar edad
#edad = int(input("ingresar su edad:"))
#if edad < 18:
    #print ("es menor de edad")
#elif 18 <= edad < 65:
    #print("es adulto")
#else :
    #print ("es adulto mayor")



#ejercicio2
#print("ingrese la operacio a realizar:")
#opcion = int(input("ingresar una opcion del 1-4:"))
#a = float(input("ingrese el primer valor:"))
#b = float(input("ingrese el segundo valor:"))
#match opcion:
    #case 1: print(f"la suma es {a + b}" )
    #case 2: print(f"la resta es {a - b}")
    #case 3: print(f"el producto es {a * b}")
    #case 4: 
        #if b != 0:
            #print(f"la division es{ a / b}")
        #else:
            #print("error la division no se puede hacer")
    #case _:
        #print("No match")
#contador = 1 
#while contador < 5:
    #print(f"el valor de contador es: {contador}")
    #contador += 1
#print("contador termiando")
#suma = 0
#for i in range (1,11):
    #suma += i

#print(f"la suma total de los 10 primeros numeros: {suma}")

#i inicia en 1 , += suma compuesta
#con un ciclop for decir cuantos numeros pares hay 

#inicio = int(input("ingrese el numero inicial: "))
#fin = int(input("ingrese el numero final: "))
#contadorPares = 0
#for i in range (inicio,fin +1):
    #if i % 2 == 0:
        #contadorPares += 1
#print(f"hay {contadorPares} numeros pares.")

#funciones en python

#reutilizar codigo y dividir programas en bloques 
#def calcularAreaCuadrada():
    #lado = int(input("ingrese el lado del cuadrado:"))
    #area = lado**2
    #return area
    
#areaCuadrado = calcularAreaCuadrada()
#print(f"el area del cuadrado es: {areaCuadrado}")
#def areaRectangulo (base, altura):
    #return base * altura
#b = int(input("ingrese la base del rectangulo:"))
#a = int(input("ingrese la altura del rectangulo:"))
#print(f"el area del rectangulo es: {areaRectangulo (b, a)~~~~~ 


#listas  

my_list=[]
print("lista completa", my_list)
print("el primer elemento es:", my_list[0])
print("el primer elemento es:", my_list[3])
print("el ultimo elemento es:", my_list[0])
lenguajes = {"python","java","c++"}
print(lenguajes)
A={1,2,3,4}
B={3,4,5,6}
print(A - B)
print(B -  A)
print(B &  A)

lista = [1,2,3,3,3,3,3,3,3,5,6,8,9,9,9]
conjunto = set(lista)
print(conjunto)
print ("python"in lenguajes )