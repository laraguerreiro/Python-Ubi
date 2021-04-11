# Exercício 3 - Cálculo Estatístico
# Escrever uma função que calcule a média e o desvio padrão de uma lista de dados
# amostrais.


# Média
from numpy import array
import statistics as st
def media (amostra):
    media = sum(amostra)/ len(amostra)
    return media


teste = [10, 20, 30, 40]


print (media(teste) )
print (st.mean(teste))

# variancia

def variancia (amostra):
    m = media(amostra)
    somadoselementos = 0
    for elemento in amostra: 
        calculo = (elemento - m) ** 2
        somadoselementos = somadoselementos + calculo
    variancia = somadoselementos / (len(amostra) - 1)
    return variancia

def desvio_padrao (amostra):
    return variancia(amostra) ** (1/2)

print (variancia(teste))
print (st.variance(teste))
print (desvio_padrao(teste))
print (st.stdev(teste))

def resposta_exercicio(amostra):
    print ("A média da amostra é igual a: ", media(amostra))
    print ("O desvio padrão é igual a: ", desvio_padrao(amostra))

resposta_exercicio(teste)

kabung = [6,7,88,65, 34]

resposta_exercicio(kabung)