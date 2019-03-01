print("Solucion en rango del 1 al 20")
for j in range(1,21):
    #condicion para multiplos de 3 y 5
    if j%3==0 and j%5==0:
        print("FizzBuzz")
    #Condicion para multiplos de 3
    elif j%3==0:
        print("Fizz")
    #Condicion para multiplos de 5
    elif j%5==0:
        print("Buzz")
    else:
        print(j)
#Codigo de Jorge Emilio Leon Vivas
