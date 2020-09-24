'''El programa debe ordenar de menor a mayor 3 numeros
ingresados por el usuario'''

#mensaje de bienvenida
print ("Bienvenido, ingrese 3 numeros distintos")
bucle = True
while (bucle == True):
    #solicito que ingrese los numeros
    a = input("Ingrese el primer numero: ")
    b = input("Ingrese el segundo numero: ")
    c = input("Ingrese el tercer numero: ")
    #valido que sean numeros y ejecuto el bucle hasta que ingrese numeros
    try:
        float(a)
        float(b)
        float(c)
    except ValueError:
        print ("No ingresaste un numero!")
    else:
    #si es numero y no son distintos los comparo entre si
        if (a!=b and b!=c and c!=a):
            if (a>b):
                if (b>c):
                    print ("El menor es ", c,", el siguiente es", b,"y el mayor es ", a)
                    bucle=False
                else:
                    if (a>c):
                        print ("El menor es ", b,", el siguiente es", c,"y el mayor es ", a)
                        bucle=False
                    else:
                        print ("El menor es ", b,", el siguiente es", a,"y el mayor es ", c)
                        bucle=False
            else:
                if (a>c):
                    print ("El menor es ", c,", el siguiente es", a,"y el mayor es ", b)
                    bucle=False
                else:
                    if (b>c):
                        print ("El menor es ", a,", el siguiente es", c,"y el mayor es ", b)
                        bucle=False
                    else:
                        print ("El menor es ", a,", el siguiente es", b,"y el mayor es ", c)
                        bucle=False
        #si son numeros iguales ejecuto el bucle hasta que ingrese numeros distintos
        else:
            print ("Intentelo nuevamente, los numeros ingresados son iguales")
            bucle=True


#Sumo los valores ingresados y muestro su resultado y su promedio
d=int(a)
e=int(b)
f=int(c)
suma=(d+e+f)
promedio=(suma/3)
print(f"al sumarlos a todos nos da {suma} y su media es {promedio}")
