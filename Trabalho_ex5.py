# Exercício 5
#Criar dicionário com 5 alunos
#cada aluno precisa ter Nome; data de nascimento; curso; cadeiras
#Escrever função para apagar determinado aluno da base
#Escrever função para inserir alunos na base

#base
aluno1 = {"nome": "Anah", "dt_nasc": "02/02/2002", "curso": "biologia", "cadeiras": ["ab", "cd", "ef"]}
aluno2 = {"nome": "Boby", "dt_nasc": "03/03/2002", "curso": "biologia", "cadeiras": ["ab", "cd", "ef"]}
aluno3 = {"nome": "Carl", "dt_nasc": "04/04/2002", "curso": "biologia", "cadeiras": ["ab", "cd", "ef"]}
aluno4 = {"nome": "Dian", "dt_nasc": "05/05/2002", "curso": "biologia", "cadeiras": ["ab", "cd", "ef"]}
aluno5 = {"nome": "Earl", "dt_nasc": "06/06/2002", "curso": "biologia", "cadeiras": ["ab", "cd", "ef"]}

base = [aluno1, aluno2, aluno3, aluno4, aluno5]


# apagar aluno
def exibir (base):
    posicao = 1
    for aluno in base:
        linha = "ID: "+ str(posicao) + " | "
        for key, value in aluno.items():
            linha = linha +str(value)
            linha = linha +" | "
        print (linha)
        posicao = posicao + 1 

# exibir (base)

def apagar_aluno (base):
    posicao = int(input("Digite o ID do aluno a ser excluído da base: "))
    base.pop(posicao - 1)
    print ("Estudante removido(a)!")
    return base

#exibir (base)
#base = apagar_aluno (base)
#exibir (base)

# Adicionar aluno

def adicionar (base):
    novo_aluno = {}
    novo_aluno ["nome"] = input ("Digite o nome: ")
    novo_aluno ["dt_nasc"] = input ("Digite a data de nascimento: ")
    novo_aluno ["curso"] = input ("Digite o curso: ")
    cadeiras = input("Digite as cadeiras, separadas por vírgula: ")
    novo_aluno ["cadeiras"] = cadeiras.split (",")
    base.append(novo_aluno)

    print ("Aluno(a) " + novo_aluno["nome"] + " adicionado(a).")
    return base

#base = adicionar (base)
#exibir (base)

# MENU para manipular a base

sair = False
while sair == False:
    print ("#### Exercício 5 - ")
    print("### Escolha uma opção ###")
    print("|1| Listar")
    print("|2| Apagar")
    print("|3| Adicionar")
    print("|0| Sair")
    opcao = int(input("Digite sua opção: "))

    if(opcao == 1):
        exibir (base)
    if (opcao == 2):
        base = apagar_aluno(base)
    if (opcao == 3):
        base = adicionar (base)
    if (opcao == 0):
        sair = True
        print ("Fim")
    input ("Pressione <Enter> para continuar...")