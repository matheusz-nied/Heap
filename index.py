import util
from HeapSort import HeapSort
import sys

# Altera o limite de recursão do Python
sys.setrecursionlimit(6000)

paths = util.list_files()

i = 0
for path in paths:
    print(i, "- " + path)
    i += 1

print("Escolha um arquivo para ser ordenado(digite o número dele):")
file = int(input())

array = util.open_file(paths[file])



tempo, comparacao, troca = HeapSort(array)


util.print_array(array)

print(f'Tempo: {tempo}, Comparacao: {comparacao}, Troca: {troca}')