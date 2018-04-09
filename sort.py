#   Djorkaeff Alexandre - Lucas Brilhante
#   Trabalho 2 - Estrutura de dados 2
#   Algorítmo de ordenação (O(n*log(n)))

import matplotlib.pyplot as plt
import random
import time
import timeit

def swap(vetor, i, j):                    
    vetor[i], vetor[j] = vetor[j], vetor[i] 

def heapify(vetor, end,i):   
    l=2 * i + 1  
    r=2 * (i + 1)   
    max=i   
    if l < end and vetor[i] < vetor[l]:   
        max = l   
    if r < end and vetor[max] < vetor[r]:   
        max = r   
    if max != i:   
        swap(vetor, i, max)   
        heapify(vetor, end, max)   

def heap_sort(vetor):     
    end = len(vetor)   
    start = end // 2 - 1 # use // instead of /
    for i in range(start, -1, -1):   
        heapify(vetor, end, i)   
    for i in range(end-1, 0, -1):   
        swap(vetor, i, 0)   
        heapify(vetor, i, 0)  

def particao(a, ini, fim):
    pivo = a[fim-1]
    start = ini
    end = ini
    for i in range(ini,fim):
        if a[i] > pivo:
            end += 1
        else:
            end += 1       
            start += 1
            aux = a[start-1]
            a[start-1] = a[i]
            a[i] = aux
    return start-1
        
def quickSort(a, ini, fim):
    if ini < fim:
        pp = randparticao(a, ini, fim)
        quickSort(a, ini, pp)
        quickSort(a, pp+1,fim)
    return a
        
def randparticao(a,ini,fim):
    rand = random.randrange(ini,fim)
    aux = a[fim-1]
    a[fim-1] = a[rand]
    a[rand] = aux
    return particao(a,ini,fim)

def generateVector(total, vetor, typeSort):
    print('Gerando vetor de números randômicos com %d números...' % total)
    vetor = random.sample(range(1, 10000000), total)
    print('Ordenando o vetor...')
    if typeSort==1:
        print('Heap-Sort')
        heap_sort(vetor)
    if typeSort==2:
        print('Quick-Sort')
        quickSort(vetor,0,len(vetor))
    print('Vetor ordenado')

def timeToSort(qtd, tempos, vetor, typeSort):
    inicio = timeit.default_timer()
    generateVector(qtd, vetor, typeSort)
    fim = timeit.default_timer()
    tempos.append(fim-inicio)
    print('Tempo para ordenação: ' + str(fim-inicio) + ' s')

def main(typeSort):
    tempos = []
    vetor = []
    tamVetor = []
    for i in range(0,30001,5000):
        tamVetor.append(i)
        timeToSort(i, tempos, vetor, typeSort)
        print('\n')
        print('Processo concluído..')
        print('\n\n\n')
    # plot(tamVetor, tempos, 'bo')                     # draw the points
    plt.plot(tamVetor, tempos)

print('1 - Ordenação com heap-sort')
print('2 - Ordenação com quick-sort')
print('3 - Ordenação com heap-sort e com quick-sort')
entrada = int(input('Digite a opção escolhida: '))
if entrada==1:
    main(1)
elif entrada==2:
    main(2)
elif entrada==3:
    main(1)
    main(2)

plt.xlabel('Tamanho vetor')
plt.ylabel('Tempo (s)')
plt.legend(['Quick-Sort', 'Heap-Sort'])
plt.grid(True)
plt.show()