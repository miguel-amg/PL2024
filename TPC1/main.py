# Criado por Miguel Guimarães
# Universidade do Minho 23/24
# Processamento de Linguagens

###################### Abrir o csv e ler conteudo ######################
ficheiro = open("emd.csv", "r")
conteudo = ficheiro.read()

###################### Processar o conteudo ######################
linhas = conteudo.split('\n') # Dividir as linhas
linhas.pop(0)                 # Remover a linha com o nome dos dados
linhas.pop()                  # Remover o ultimo elemento (Elemento sem dados devido a '\n' final)

###################### Preencher os arrays com os dados ######################
# Arrays para preencher com dados
modalidades = []   # Array para as modalidades
estadoAtletas = [] # Array para o estado dos atletas (Apto - inapto)
idadesAtletas = [] # Array para as idades dos atletas

# Percorrer as linhas
for linha in linhas:
    dados = linha.split(',') # Dados da linha atual
    modalidades.append(dados[8]) # Adicionar a modalidade à lista de modalidades
    estadoAtletas.append(dados[12]) # Adiciconar o estado do atleta à lista de estados
    idadesAtletas.append(dados[5]) # Adiciconar a lista das idades dos atletas

###################### Realização das tarefas ######################
# Primeira tarefa: Lista ordenada alfabeticamente das modalidades desportivas
modalidades = list(set(modalidades)) # Remove modalidades repetidas
modalidades.sort()                   # Ordenar as modalidades

# Segunda tarefa: Percentagens de atletas aptos e inaptos para a prática desportiva
total_atletas = 0
aptos = 0
inaptos = 0

# Obter as quantias
for estado in estadoAtletas:
    if estado == "true":
        aptos += 1
    else:
        inaptos += 1

    total_atletas += 1

# Obter as percentagens
taxa_aptos = aptos/total_atletas
taxa_inaptos = inaptos/total_atletas

# Terceira tarefa: Distribuição de atletas por escalão etário (escalão = intervalo de 5 anos): ... [30-34], [35-39], ...
escaloes = {}
idadesAtletas.sort()

for idade in idadesAtletas:
    escalaoRAW = int(idade)/5    # Dividir em escaloes
    escalao = int(escalaoRAW)    # Remover decimas

    entrada = "[" + str(escalao*5) + "," + str(escalao*5 + 4) + "]"

    # Verificar se a chave existe no dicionario
    if entrada in escaloes:
        escaloes[entrada] += 1 # Chave existe no dicionario
    else: 
        escaloes[entrada] = 1 # Chave nao existe no dicionario ainda

###################### Print dos resultados ######################
print("Lista de modalidades: " + str(modalidades))
print("Percentagem de aptos: " + str(taxa_aptos))
print("Percentagem de inaptos: " + str(taxa_inaptos))
print("Distribuicao por escalao:" + str(escaloes))

