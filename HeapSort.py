import util
import time


def PAI(i):
    return int((i - 1) / 2)


def ESQ(i):
    return int(i*2 + 1)


def DIR(i):
    return int((2*i) + 2)


def constroi_heap(array, tam, quantidade_comparacao, quantidade_troca):
    i = tam
    quantidade_comparacao[0] += 1
    while(i >= 0):
        quantidade_comparacao[0] += 1

        i -= 1
        #i = PAI(i)
        heapifica(array, i, tam, quantidade_comparacao, quantidade_troca)
        if(i == 0):
            quantidade_comparacao[0] += 1

            break


def heapifica(array, i, tam, quantidade_comparacao, quantidade_troca):
    maior = i
    left = ESQ(i)
    right = DIR(i)

    quantidade_comparacao[0] += 1
    
    if(left < tam and array[left][0] > array[maior][0]):
        maior = ESQ(i)
        
    quantidade_comparacao[0] += 1
    if(right < tam and array[right][0] > array[maior][0]):
        maior = DIR(i)

    quantidade_comparacao[0] += 1
    if(maior != i):
        quantidade_troca[0]+=1 
        util.troca(array, i, maior)
        heapifica(array, maior, tam, quantidade_comparacao, quantidade_troca)


def HeapSort(array):
    tempo_gasto = 0
    quantidade_comparacao = [0]
    quantidade_troca = [0]
    ini = time.time()
    tam = util.count_array(array)

    constroi_heap(array, tam, quantidade_comparacao, quantidade_troca)
    for i, element in reversed(list(enumerate(array))):
        util.troca(array, i, 0)
        quantidade_troca[0]+=1 
        heapifica(array, 0, i, quantidade_comparacao, quantidade_troca)
        if(i == 1):
            break

    fim = time.time()
    tempo_gasto = fim - ini
    return tempo_gasto, quantidade_comparacao, quantidade_troca
