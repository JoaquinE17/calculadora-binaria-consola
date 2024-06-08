import os
import time
import menu_iterativo
import operaciones_binarias

def continuar():
    pasiencia=0
    seguir=input(">_Continuar operando [S] o [N]: ").lower()
    if seguir!='s' or seguir!='n':
        while seguir!='s' and seguir!='n' and pasiencia<3:
            print("Opcion incorrecta..")
            seguir=input(">_Solo se permite [S] o [N]: ").lower()
            pasiencia+=1
        if pasiencia==3 and seguir!='s' and seguir!='n':
            print(">_Pasiencia colmada..")
            return 'n'
    return seguir
            
#MAIN__________________________________________________________________________

while(True):
    seleccion=menu_iterativo.CursorSelector()
    match seleccion:
        case 0:
            try:
                num=int(input(">_Ingrese binario a operar: "))
                print(f"  El {num} en desimal es: {operaciones_binarias.BiDe(num)}")
            except ValueError:
                print("Error: Debes ingresar un numero binario.")
        case 1:
            try:
                num=int(input(">_Ingrese numero a operar: "))
                print(f"  El {num} en binario es: {operaciones_binarias.DeBi(num)}")
            except ValueError:
                print("Error: Debes ingresar un número entero.")
        case 2:
            try:
                num1=int(input("1° Ingrese Sumando: "))
                num2=int(input("2° Ingrese sumando: "))
                print(f"El resultado de la suma binaria es: {operaciones_binarias.SuBi(num1,num2)}")
            except ValueError:
                print("Error: Ambos números deben ser bianarios .")
        case 3:
            try:
                num1=int(input("1° Ingrese Minuendo: "))
                num2=int(input("2° Ingrese Sustraendo: "))
                print(f"El resultado de la resta binaria es: {operaciones_binarias.Rebi(num1,num2)}")
            except ValueError:
                print("Error: Ambos números deben ser bianarios .")
        case 4:
            try:
                num1=int(input("1° Ingrese Multiplicando: "))
                num2=int(input("2° Ingrese Multiplicador: "))
                print(f"El resultado de la multiplicacion binaria es: {operaciones_binarias.MuBi(num1,num2)}")
            except ValueError:
                print("Error: Ambos números deben ser bianarios .")
        case 5:
            try:
                num1=int(input("1° Ingrese Dividendo: "))
                num2=int(input("2° Ingrese Divisor: "))
                print(f"El cociente de la divicion binaria es: {operaciones_binarias.DiBi(num1,num2)}")
            except ValueError:
                print("Error: Ambos números deben ser bianarios .")
        case 'q':
            break
    son=continuar()
    if son=='s' or son=='n':
        if (son=='n'):
            print("Saliendo..")
            time.sleep(.5)
            break
        elif (son=='s'):           
            os.system("cls")