import util
from HeapSort import HeapSort
import sys

# Altera o limite de recursão do Python
sys.setrecursionlimit(6000)

paths = util.list_files()

i = 0
for path in paths:
    array = util.open_file(path)
    tempo, comparacao, troca = HeapSort(array)
    print(f' File {path} - Tempo: {tempo}, Comparacao: {comparacao}, Troca: {troca}')






