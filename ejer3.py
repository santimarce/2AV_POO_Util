#Imprima el patrón con el ciclo for
#*
#**
#***
#****
#*****
#****
#***
#**
#*
def patron(c):    
    for i in range(1,6):
        c=c+'*'
        print(c)
    for j in range(1,5):
        c = c[:-1]
        print(c)
         
dibujo = patron('00000')