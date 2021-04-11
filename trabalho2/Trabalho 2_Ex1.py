from numpy import array, transpose
from numpy.linalg import det, inv, eig

D = array([[3.4, 0.5, 1.2, -0.8],
    [-1.6, 6.8, 1.1, 2.3],
    [0.1, -0.5, 2.5, 0.7],
    [-0.9, 1.7, 0.2, 4.9]])

print("Matriz D")
print(D)

# Calcular a matriz A = D.Dt
DT = transpose(D)
print("Matriz DT")
print(DT)

A = D.dot(DT)
print("Matriz A")
print(A)

# 2. Calcular a determinante da matriz A. Qual a inversa da matriz A?

determinante_A = det (A)
print ("A Determinante de A é igual a " + str(determinante_A)) 

inversa_A = inv(A)
print ("A Inversa de A é igual a =" + str(inversa_A))

# 3. Calcular os valores e vetores próprios (autovalores e autovetores) da matriz A.

w, v= eig(A)
print( "Valores - autovalores - da matriz A = " + str(w))
print ("Os vetores próprios - autovetores - da matriz A = " +str(v))