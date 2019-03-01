print("Solucion en rango del 1 al 20")
for j in range(1,21):
    #Condicion para multiplos de 3
    if j%3==0:
        print("Fizz")
    #Condicion para multiplos de 5
    elif j%5==0:
        print("Buzz")
    else:
        print(j)
