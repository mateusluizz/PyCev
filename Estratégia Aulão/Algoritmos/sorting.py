def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j+1] = lista[j]
            j -= 1
        lista[j+1] = chave


def bubble_sort(lista):
    n = len(lista)
    for j in range(n-1):
        for i in range(n-1):
            if lista[i] > lista[i+1]:
                # troca de elementos na posição i e i+1
                lista[i], lista[i+1] = lista[i+1], lista[i]
# Complexidade de tempo O(nˆ2)
# Complexidade de espaço O(n)


def selection_sort(lista):
    n = len(lista)
    for j in range(n-1):
        min_index = j
        for i in range(j, n):
            if lista[i] < lista[min_index]:
                min_index = i
        if lista[j] > lista[min_index]:
            aux = lista[j]
            lista[j] = lista[min_index]
            lista[min_index] = aux
# 1 + (n-1)*[5 + X] = 1 + 5*(n-1) + X*(n-1)
# Complexidade de tempo O(nˆ2)
# Complexidade de espaço O(n)


def bubble_reverse(dado):
    for passnum in range(len(dado)-1, 0, -1):
        for i in range(passnum):
            if dado[i] > dado[i+1]:
                temp = dado[i]
                dado[i] = dado[i+1]
                dado[i+1] = temp


dado = [16, 18, 15, 37, 13]
bubble_reverse(dado)
print(dado)



