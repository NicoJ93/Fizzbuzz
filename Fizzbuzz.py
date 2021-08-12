def fizzbuzz(num):
    num = num
    contador = 0
    while contador <= num:
        if contador % 3 == 0 and contador % 5 == 0 and contador != 0:
            print ("Fizzbuzz")
        elif contador % 3 == 0 and contador != 0:
            print ("Fizz")
        elif contador % 5 == 0 and contador != 0:
            print ("Buzz")
        else:
            print (contador)
        contador += 1

num = int(input("Ingrese un número: "))

fizzbuzz(num)
