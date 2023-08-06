#Validación y operaciones de datos

#Crear un programa, que tenga en su sintaxis estructuras de control de flujo y que 
#almacene datos en listas, tuplas o diccionarios, con los siguientes retos.

#  1.- Longitud de una frase:
#   Crear un programa para identificar la longitud de una palabra ingresada. La
#   palabra correcta debe tener entre cuatro y ocho letras. toma en cuenta las
#   siguientes consideraciones:
   
#     * Si la longitud de la palabra se encuentra en el rango de cuatro a ocho
#       letras, se debe imprimir un mensaje que indique que la palabra es correcta.

#     * Si la palabra tiene menos de 4 letras debe indicar un mensaje que diga: 
#       Hacen falta letras. Solo tiene N letras (siendo N el número de letras de la palabra).

#     * Si la palabra tiene más de 8 letras debe indicar un mensaje que diga:
#       Sobran letras. Tiene N letras (siendo N el número de letras de la palabra).

print("\n\t\t1.- Longitud de una frase.\n")                                                             #Manda mensaje sobre el primer reto.
palabra= str(input("Ingresa la palabra : "))                                                            #Declara y guarda el str ingresasdo en la variable 'palabra'

while True :                                                                                            #Se inicia un ciclo while 
    
    if len(palabra)>=4 and len(palabra)<=8:                                                             #Se compara el tamaño de la palabra que contenga de 4 a 8 letras,
        print("\nEl tamaño de la palabra es correcto")                                                  #manda mensaje si el tamaño es el indicado y
        print(f"La cantidad de letras es :",len(palabra))                                               #muestra el tamaño de la palabra ingresada.
        
        if len(palabra)==7:                                                                             #Compara si el tamaño de la palabra es de 7 letras y manda mensaje de
            print(f"Estuviste a ",8-len(palabra)," letra para el maximo de letras permitidas")          #cuantas letras faltaron para el maximo permitido.
        
        elif len(palabra)>=4 and len(palabra)<=6:                                                       #Compara si el tamaño de la palabra es de 4 a 6 letras y manda mensaje de
            print(f"Estuviste a ",8-len(palabra)," letras para el maximo de letras permitidas")         #cuantas letras faltaron para el maximo permitido.
        
        else :                                                                                          #Si el tamaño de la palabra es de 8 letras manda mensaje y muestra el
            print(f"Estas en el maximo de letras permitidas que es ",len(palabra))                      #tamaño de la palabra

        break                                                                                           #Sale de la iteración while.

    elif len(palabra)==3:                                                                               #Compara que el tamaño de la palabra sea igual a 3, manda mensaje por el
        print("\nEl tamaño de la palabra es muy corto")                                                 #tamaño corto de la palabra, muestra el tamaño y pide que vuelva a  
        print(f"La cantidad de letras es : ",len(palabra))                                              #ingresar la palabra con el tamaño permitido.
        print("Te falto 1 letra para al canzar el minimo de 4 letras permitidas")
        palabra=str(input("Vuelve a intentarlo :  "))
        continue                                                                                        #Vuelve a iterar.

    elif len(palabra)<=2:                                                                               #Compara que el tamaño de la palabra sea igual o menor a 2, manda mensaje
        print("\nEl tamaño de la palabra es muy corto")                                                 #por el tamaño corto de la palabra, muestra el tamaño y pide que vuelva a
        print(f"La cantidad de letras es : ",len(palabra))                                              #ingresar la palabra con el tamaño permitido.
        print(f"Te faltaron ",4-len(palabra)," letras para alcanzar el minimo de 4 letras permitidas")
        palabra=str(input("Vuelve a intentarlo :  "))
        continue                                                                                        #Vuelve a iterar.

    else :                                                                                              #Solo si la palabra sobrepasa el tamaño permitido, manda mensaje, muestra
        print("\nEl tamaño de la palabra es muy largo")                                                 #el tamaño de la palabra y pide que vuelva a ingresar la palabra con el 
        print(f"La cantidad de letras es : ",len(palabra))                                              #tamaño permitido.
        print(f"Te sobraron :",len(palabra)-8," letras para alcanzar el maximo de 8 letras permitidas")
        palabra=str(input("Vuelve a intentarlo :  "))
        continue                                                                                        #Vuelve a iterar.

# 2.- Encuentre el cuadrante:

#  Crear un programa que en base a 2 números de entrada, coordenadas,
#  identifique en cuál de los 4 cuadrantes se encuentra el punto. El programa
#  debe verificar que NINGUNA coordenada sea 0

print("\n\t\t2.- Encuentra el cuadrante.")                                                              #Manda mensaje sobre el segundo reto.
print("\nPuedes ingresar tus coordenadas como numeros enteros o con decimales")                         #Manda mensaje.
coorx=float(input("\nIngresa la coordenada del eje X :  "))                                             #Declara las variables 'coorx' y 'coory'.
coory=float(input("\nIngresa la coordenada del eje Y :  "))                                             #Pide que se ingrese un valor a las variables.
cuad=str                                                                                                #Declara variable 'cuad' como string.

while True:                                                                                             #Se inicia un ciclo while
    
    if coorx==0:                                                                                        #Se compara que coorx sea igual a 0.
        print("\nLo siento pero ninguna coordenada puede ser CERO")                                     #Manda mensaje y pide que se vuelva a ingresar la coordenada X.
        coorx=float(input("\nVuelve a ingresar la coordenada del eje X :  "))
        continue                                                                                        #Vuelve a iterar.
    
    if coory==0:                                                                                        #Se compara que coory sea igual a 0.
        print("\nLo siento pero ninguna coordenada puede ser CERO")                                     #Manda mensaje y pide que se vuelva a ingresar la coordenada Y.
        coory=float(input("\nVuelve a ingresar la coordenada del eje Y :  "))
        continue                                                                                        #Vuelve a iterar.

    elif coorx>0 and coory>0:                                                                           #Cuadrante 1 compara que las coordenadas sean mayores a 0.
        print("\nTe encuentras en el PRIMER CUADRANTE ")                                                #Manda mensaje y muestra las coordenadas ingresadas.
        print(f"Tus coordenadas son en X : ",coorx," en Y : ",coory)                                    #Asigna un string a la variable cuad.
        cuad='PRIMERO'
        break                                                                                           #Sale de la iteración while.

    elif coorx<0 and coory>0:                                                                           #Cuadrante 2 compara que 'Y' sea mayor a 0 y que 'X' sea menor a 0.
        print("\nTe encuentras en el SEGUNDO CUADRANTE ")                                               #Manda mensaje y muestra las coordenadas ingresadas.
        print(f"Tus coordenadas son en X : ",coorx," en Y : ",coory)                                    #Asigna un string a la variable cuad.
        cuad='SEGUNDO'
        break                                                                                           #Sale de la iteración while.

    elif coorx<0 and coory<0:                                                                           #Cuadrante 3 compara que 'Y' sea menor a 0 y que 'X' sea menor a 0.
        print("\nTe encuentras en el TERCER CUADRANTE  ")                                               #Manda mensaje y muestra las coordenadas ingresadas.
        print(f"Tus coordenadas son en X : ",coorx," en Y : ",coory)                                    #Asigna un string a la variable cuad.
        cuad='TERCERO'
        break                                                                                           #Sale de la iteración while.

    else :                                                                                              #Cuadrante 4 'Y' es menor a 0 y 'X' es mayor a 0.
        print("\nTe encuentras en el CUARTO CUADRANTE  ")                                               #Manda mensaje y muestra las coordenadas ingresadas.
        print(f"Tus coordenadas son en X : ",coorx," en Y : ",coory)                                    #Asigna un string a la variable cuad.
        cuad='CUARTO'
        break                                                                                           #Sale de la iteración while.

datos={'Palabra =>':palabra,'Coordena X =>':coorx,'Coordenada Y =>':coory,'Cuadrante =>':cuad}          #Se declara un diccionario que contenga los datos ya ingresados.
print("\nHice un directorio con los datos que me proporcionaste ;D \n")                                 #Se manda mensaje a pantalla.

for clave,valor in datos.items():                                                                       #Se declara un ciclo for para imprimir el diccionario.
    print(clave,valor)

exit()                                                                                                  #Fin del programa.