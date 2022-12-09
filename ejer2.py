#imprimir un patron con el ciclo for
#5 4 3 2 1
#4 3 2 1
#3 2 1
#2 1
#1
#Santiago Venegas - Segundo "A"
def lista(c):
    for i in range(1,6):
        print(c)
        c = c.lstrip(c[0])
        
operacion = lista('54321')