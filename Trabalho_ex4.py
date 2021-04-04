# Exercício 4
#1. Escrever a função que afixe os n primeiros elementos desta sucessão.
#2. Lista dos n primeiros elementos da sucessão
#3. Escrever função que devolva a soma dos n primeiros elementos.
#4. Escrever uma função que devolva o k-gésimo elemento da sucessão (k escolhido.)

#OBS para o prof. Estamos considerando que a posição 0 é igual a 0

#1. 
n = int (input ("Quantos elementos da sucessão (Fibonacci) deseja saber? "))

def lista (n):
    fibonacci = [1, 1]
    posicao = 2

    while n > 2:
        um_passo = fibonacci [posicao - 1]
        dois_passos = fibonacci [posicao - 2]
        fibonacci.append (um_passo + dois_passos)
        posicao = posicao + 1
        n = n - 1
    return fibonacci

# 2.
fibonacci = lista(n)

print (fibonacci)    

#3.
def soma (fibonacci):
    total = 0
    for valor in fibonacci:
        total = total + valor
    return total

print ( "A soma das " + str(n) + " posições da sequencia é igual a " + str(soma(fibonacci)) +".")

#4.
def kgesimo(k):
    fibonacci = lista (k+1)
    return fibonacci [-1]
k = int(input("Qual o k-gésimo elemento que deseja saber? "))
print ("O k-gésimo elemento requerido é o " + str(kgesimo(k)) )

#