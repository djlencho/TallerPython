numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

numero = int(input("Ingrese un número: "))

if numero > 20:
    print("El número es mayor que 20.")
elif numero < 20:
    print("El número es menor que 20.")
else:
    print("El número es igual a 20.")

##condicion que evalue dos posibilidades
año = int(input("Ingrese un año: "))

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print(año, "es un año bisiesto.")
        else:
            print(año, "no es un año bisiesto.")
    else:
        print(año, "es un año bisiesto.")
else:
    print(año, "no es un año bisiesto.")