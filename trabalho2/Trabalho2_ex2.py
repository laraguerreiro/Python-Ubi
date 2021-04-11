import math
from numpy import arange, max, min, array


#1. Escrever um programa que crie uma matriz M com os valores de z= f(x,y) 
# para o intervalo [-2,2] comum passo de 0.1 e y no intervalo [-3, 3], com passo de 0.2 .

def fxy (x,y):
    resultado = 0.1 + ( (1 + math.sin(2*x + 3*y)) / (3.5 + math.sin(x-y)) )
    return resultado

def cria_matriz ():
    matriz_M =[]

    for x in arange (-2,2,0.1):
        linha = []
        for y in arange(-3,3,0.2):
            valor = fxy(x,y)
            linha.append(valor)
        matriz_M.append(linha)
    return matriz_M
M = cria_matriz()

print("A matriz M é igual a ")
print (M)



# 2. Qual é o menor elemento da sexta coluna da Matriz M?

x = M[:][5]

xmin = min(x)

print( "O menor elemento de sexta coluna " + str(xmin) )

# 3. Qual o menor elemento da Matriz M

y = M[:][:]
ymin = min(y)
print ("O menor valor da Matriz M é igual a " + str(ymin))

# 4. Qual é o maior elemento da matriz M?


ymax = max(y)
print("O maior elemento da Matriz M é igual a " + str(ymax))


