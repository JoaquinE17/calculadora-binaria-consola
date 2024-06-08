import os
import time 
#import keyboard(Implementacion -> Version 2)

def CursorSelector():
    os.system("cls")
    opciones=["Convertir Binario a Desimal","Convertir Desimal a Binario","Sumar Binarios","Restar Binarios","Multiplicar Binarios","Dividir Binarios"]
    flecha="<<<<"
    titulo="*****CALCULADORA BASICA BINARIA*****"
    espacio="."
    n=0
    while True:
        print(titulo)
        for i, j in enumerate(opciones):
            for k in range(1):
                if i==n:
                    Cesp=len(titulo)-(len(opciones[n])+len(flecha))
                    print(f"{opciones[n]}{espacio*Cesp}{flecha}")
                else:
                    print(j)
        print("-"*len(titulo))
        accion=input("W(subir)/S(bajar)Q(salir)/A(elegir): ").lower()
        if accion=='s':
            n+=1
            if n==len(opciones):
                n=len(opciones)-1
            while True:
                os.system("cls")
                break
        elif accion=='w':
            n-=1
            if n<1:
                n=0
            while True:
                os.system("cls")
                break
        elif accion=='q':
            print("Saliendo..")
            time.sleep(.5)
            return 'q'
        elif accion=='a':
            print("-"*len(titulo))
            print(f"*****{opciones[n]}*****")
            return n
        else:
            print("Opcion incorrecta..")
            while True:
                time.sleep(.4)
                os.system("cls")
                break
