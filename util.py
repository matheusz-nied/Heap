import os
import csv


def list_files():
    pasta = './'
    paths = []

    for diretorio, subpastas, arquivos in os.walk(pasta):
        for arquivo in arquivos:
            if arquivo.lower().endswith(".csv"):
                paths.append(os.path.join(diretorio, arquivo))

    return paths


def open_file(path):
    arquivo = open(path)

    file = csv.reader(arquivo)
    array = list(file)
    array.pop(0)
    return array


def count_array(file):
    count = 0
    for linha in file:
        count += 1
    return count


def print_array(array):
    for line in array:
        print(line)

def troca(array, indice1, indice2):
    aux = array[indice1]
    array[indice1] = array[indice2]
    array[indice2] = aux