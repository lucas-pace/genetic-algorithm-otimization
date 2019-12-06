# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""
POPULACAO_SIZE = 100;
PESO_MAXIMO = 5000;
## Mochila[espaco i] composta por (peso, utilidade)
## F objetivo maximizar utilidade da mochila
## peso < 5000

import random


class Individuo:
    def __init__(self, mochila):
        self.qtd = []
        self.mochila = mochila
        self.pesoTotal = 0
        self.utilidade = 0
        
    def aleatorioInicial(self):
        self.qtd.clear()
        for i in range(len(self.mochila.items)):
            self.qtd.append(random.randint(0, int(PESO_MAXIMO/self.mochila.items[1].att[0])))
        self.calculaPesoTotal()
        self.calculaUtilidade()
        self.novoIndividuo()
            
            
    def novoIndividuo(self):
        sum = 0
        for i in range(len(self.qtd)):
            sum += (self.mochila.items[i].att[0]*self.qtd[i])
        if(sum < PESO_MAXIMO):
            return 1
        else:
            self.aleatorioInicial()
        
    def viabilidade(self):
        sum = 0
        for i in range(len(self.qtd)):
            sum += (self.mochila.items[i].att[0]*self.qtd[i])
        if(sum < PESO_MAXIMO):
            return True
        else:
            return False
            
    def calculaPesoTotal(self):
        sum = 0
        for i in range(len(self.qtd)):
            sum += (self.mochila.items[i].att[0]*self.qtd[i])
        self.pesoTotal = sum
        return sum
    
    def calculaUtilidade(self):
        sum = 0
        for i in range(len(self.qtd)):
            sum += (self.mochila.items[i].att[1]*self.qtd[i])
        self.utilidade = sum
        return sum
        

class Item:
    def __init__(self, peso, utilidade):
        self.att = (peso, utilidade)
        
class Mochila:
    def __init__(self):
        self.items = []
        
    def addItem(self,item):
        self.items.append(item)

def mutacaoAux(individuo):
    gene = random.randint(0,len(individuo.qtd)-1)
    individuo.qtd[gene] = random.randint(0, int(PESO_MAXIMO/individuo.mochila.items[1].att[0]))
    if individuo.viabilidade():
        return 0
    else: 
        mutacaoAux(individuo)
        
def mutacao(i1,i2):
    ocorre = random.randint(0,4)
    if ocorre == 0:
        qualIndividuo = random.randint(0,1)
        if qualIndividuo == 0:
            individuo = i1
        else: 
            individuo = i2
        gene = random.randint(0,len(i1.qtd)-1)
        individuo.qtd[gene] = random.randint(0, int(PESO_MAXIMO/individuo.mochila.items[1].att[0]))
        if individuo.viabilidade():
            return 0
        else: 
            mutacaoAux(individuo)
        
    
        
def crossover(i1, i2):
    indice1 = random.randint(0,len(i1.qtd)-1)
    indice2 = random.randint(0,len(i2.qtd)-1)
    qtd1 = i1.qtd[indice1]
    qtd2 = i2.qtd[indice2]
    i1.qtd[indice1] = qtd2
    i2.qtd[indice2] = qtd1
    i1.novoIndividuo()
    i2.novoIndividuo()
    mutacao(i1,i2)
    
    
            ###  Criando items
            
item1 = Item(1,9)
item2 = Item(3,27)
item3 = Item(2,20)          
            
            ## Crindo mochila
mochila = Mochila()
            
            ### Adicionando items]
mochila.addItem(item1)
mochila.addItem(item2)
mochila.addItem(item3)

            ### Criando pop inicial
n = int( POPULACAO_SIZE/2 )


populacao = []
for i in range(POPULACAO_SIZE):
    individuo = Individuo(mochila)
    individuo.aleatorioInicial()
    populacao.append(individuo)


#Ordenando o vetor pelaa utilidade
melhorUtilidade = 0
for aux in range(10000):
    populacao.sort(key = lambda x: x.utilidade, reverse = True)
    for i in range(len(populacao)):
        populacao[i].calculaUtilidade()
        populacao[i].calculaPesoTotal()
        
    # Dividindo a populacao
    subPopulacoes = [populacao[i::2] for i in range(n)]
    populacaoMelhores = subPopulacoes[0]
    populacaoPiores = subPopulacoes[1]

    # Salva melhor utilidade
    if populacaoMelhores[0].utilidade > melhorUtilidade:
        melhorUtilidade = populacaoMelhores[0].utilidade    
        aux = 0
    
    # Escolher individuo entre os melhores para o crossovers
    escolhidoMelhor = random.randint(0,n-1)
    escolhidoPior = random.randint(0,n-1)
    
    crossover(populacaoMelhores[escolhidoMelhor], populacaoPiores[escolhidoPior])
    
print(melhorUtilidade)