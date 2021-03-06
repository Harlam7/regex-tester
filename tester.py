"""
    Tester de expresiones regulares en Python realizado por:
    - Luis David Arias
    - Nicolas Duque
"""
#Libreria de expresiones regulares
import re

#Se define un diccionario para almacenar expresiones regulares
regex = {}
#Se definen las expresiones regulares
regex[0] = re.compile('')#ER para correos electronicos
regex[1] = re.compile('')#ER para direcciones ip
regex[2] = re.compile('')#ER para tarjetas de credito
regex[3] = re.compile('')#ER para numeros binarios
regex[4] = re.compile('')#ER para numeros hexadecimales
regex[5] = re.compile('')#ER para direcciones web
regex[6] = re.compile('(/\*[^*]*[^/]*\*/)|(//.*)')#ER para comentarios

#Funcion para imprimir menu
def print_menu():
    print("Regex - Tester")
    print("Seleccione una ER para evaluar")
    print("0. Correo electronico")
    print("1. Direccion IP")
    print("2. Tarjeta de credito")
    print("3. Numero binario")
    print("4. Numero hexadecimal")
    print("5. Direccion web")
    print("6. Comentarios en C/C++")
    print("7. Salir")

#Funcion para testear un texto en una expresion regular
def testRegex(id,text):
    match = re.search(regex[id],text)#Almacenamos el resultado de la busqueda
    if(match):#Si se obtuvo un resultado diferente de None
        print(text[match.start():match.end()]+" es valido")#Imprimimos el resultado
    else:
        print("La cadena ingresada no es valida")

#Ejecucion del programa
def main():
    option = ''
    while(option != '7'):#Mientras que la opcion no sea 'Salir'
        print_menu()#Imprimimos el menu
        option = str(input('# '))#Almacenamos la opcion digitada
        print()#Salto de linea
        if(option == '0'):
            print("WIP\n")
        elif(option == '1'):
            print("WIP\n")
        elif(option == '2'):
            print("WIP\n")
        elif(option == '3'):
            print("WIP\n")
        elif(option == '4'):
            print("WIP\n")
        elif(option == '5'):
            print("WIP\n")
        elif(option == '6'):
            string = str(input("Ingrese la cadena\n>>> "))#Almacenamos la cadena ingresada
            testRegex(int(option),string)#La testeamos con su respectiva ER
        elif(option == '7'):
            print("Hasta Luego\n")
        else:
            print("Opcion no valida\n")

main()
