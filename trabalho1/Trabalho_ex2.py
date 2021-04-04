# escrever um programa que conte a ocorrência de cada vogal do alfabeto latino num texto teterminado. 
# a letra em minúsculo e a equivalente em maiúsculo são consideradas uma diferente da outra

#texto = "Várias são as formas de manipularmos um navegador Web através do Python. Talvez a maneira mais desconhecida seja a manipulação através da criação de um janela e a posterior adição do espaço que é renderizado na exibição de cada página."
texto = input ("Digite o texto para que as vogais sejam contadas: ")
vogais = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
contador = 0

for letra in texto:
    if(letra in vogais):
        contador = contador + 1
print ("Total de vogais encontradas no texto: " + str(contador))