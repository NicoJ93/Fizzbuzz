def fizzbuzz(self, num):
    num = num
    contador = 0
    while contador <= num:
        if num % 3:
            print ("Fizz")
        elif num % 5:
            print ("Buzz")
        elif num % 3 and num % 5:
            print ("Fizzbuzz")
        else:
            print (num)
        contador += 1

num = int(input("Ingrese un número: "))

fizzbuzz(num)
