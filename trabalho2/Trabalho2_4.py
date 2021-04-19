# Exercicio 4 - Escrever um programa para efetuar a análise estatística da coluna "Close":

import pandas as pd 
import statistics as st
import matplotlib.pyplot as plt 
import os
import seaborn as sns

df = pd.read_csv(os.path.join(os.path.dirname(__file__),"base_ex4.csv"))
# Abaixo teste para verificar se a importação da base funcionou corretamente.
#print (df.head()) # 5 primeiros posições
# print (df.tail()) # -5 primeiros posições

media = st.mean(df['Close'])
print("Média =", media)

moda = st.mode(df['Close'])
print("Moda =", moda)

mediana = st.median(df['Close'])
print("Mediana =", mediana)

amplitude = max(df['Close']) - min(df['Close'])
print("Amplitude =", amplitude)

quartis = st.quantiles(df['Close'])
print("A lista dos quartis é:", quartis)
Q1 = quartis[0]; Q2 =  quartis[1]; Q3 = quartis[2]
print(f"Q1 = {Q1}, Q2 = {Q2}, Q3 = {Q3}")
IQR = Q3 - Q1 
print("IQR =", Q3-Q1)





# print (df['Close'].describe()) # descrição estatística dos dados
# Na análise acima está sendo analisada toda a tabela, e serve como teste. 
# O programa deve analisar a coluna close [4].


# O histograma mostra a quantidade de vezes que a moeda fechou em determinado valor.
#seaborn 
sns.histplot(data = df, x = 'Close')
plt.title("Histograma")
plt.show() 

# Boxplot (i.e. "CAixa de bigode")
plt.boxplot(df["Close"], notch = 'True')
plt.show ()
#Informa informação visual de dos quartis da amostra, bem como de sua mediana e dispersão.



