# Exercício 5: Fazer a análise estatística dos dados da coluna 'Age' 
# da tabela no seguinte link: 	https://www.reuters.com/companies/GOOG.O/people

import requests
import pandas as pd
import statistics as st
import seaborn as sns
import matplotlib.pyplot as plt

url = "https://www.reuters.com/companies/GOOG.O/people"

wb_site_pd = requests.get(url)  
tables = pd.read_html(wb_site_pd.text) 
df = tables[0]      
print(df.head())


media = st.mean(df['Age'])
print("Média =", media)

moda = st.mode(df['Age'])
print("Moda =", moda)

mediana = st.median(df['Age'])
print("Mediana =", mediana)

amplitude = max(df['Age']) - min(df['Age'])
print("Amplitude =", amplitude)

quartis = st.quantiles(df['Age'])
print("A lista dos quartis é:", quartis)
Q1 = quartis[0]; Q2 =  quartis[1]; Q3 = quartis[2]
print(f"Q1 = {Q1}, Q2 = {Q2}, Q3 = {Q3}")
IQR = Q3 - Q1 
print("IQR =", Q3-Q1)

sns.histplot(data = df, x = 'Age')
plt.title("Histograma")
plt.show()

plt.boxplot(df["Age"], notch = 'True')
plt.show ()