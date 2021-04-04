# Programa no qual 
#a. o utilizador adivinhar um número inteiro de 0 a 9 inclusive, ( definir esse range)
#b.   escolhido aleatoriamente pelos computador. 
#c. O jogador tem 5 chances.
#d. O jogo termina ao acertar ou terminar as tentativas. 
#e. Mensagem ao final "Acertou" ou "Não acertou"

from random import randint

# sortear um número aleatório do range determinado.
# apresentar instruções para o jogador. 
# receber a tentativa.
# verificar a tentativa
# finalizar programa

numero_sorteado = randint(0,9)
acerto = False
tentativas = 5

print("Olá, tente acertar qual o número inteiro sorteado, no intervalo de 0 a 9.")
print ("Você tem direito a " + str(tentativas) +  " tentativas.") 

while tentativas > 0 and acerto==False:

    tentativa = input("Qual o número sorteado?")
    print("Você escolheu " + str(tentativa))

    if (int(tentativa) == numero_sorteado):
        acerto = True
        print ("Você acertou! O número sorteado é também " + str(numero_sorteado))

    else:
        print ("Você errou!")
    tentativas = tentativas - 1
    if (tentativas >0 and acerto == False):
        print ("Você ainda tem mais " + str(tentativas) +" tentativas")
if (acerto == False):
    print ("O número sorteado era " + str(numero_sorteado)".")







