import random
import timeit
import heapq

# ---------------- GERADOR ----------------
def gerador_aleatorio(inicial, final, numeros):
    return [random.randint(inicial, final) for _ in range(numeros)]


# ---------------- BUBBLE ----------------
def bubble_nao_otimizado(numeros):
    n = len(numeros) - 1
    for i in range(n):
        for k in range(n):
            if numeros[k] > numeros[k+1]:
                numeros[k], numeros[k+1] = numeros[k+1], numeros[k]
    return numeros


def bubble_otimizado(numeros):
    n = len(numeros) - 1
    for i in range(n):
        for k in range(n - i):
            if numeros[k] > numeros[k+1]:
                numeros[k], numeros[k+1] = numeros[k+1], numeros[k]
    return numeros


# ---------------- INSERTION ----------------
def insercao_nao_otimizado(numeros):
    for i in range(1, len(numeros)):
        for k in range(i):
            if numeros[i] < numeros[k]:
                numeros.insert(k, numeros.pop(i))
                break
    return numeros


def insercao_otimizado(numeros):
    for i in range(1, len(numeros)):
        valor = numeros[i]
        k = i - 1
        while k >= 0 and numeros[k] > valor:
            numeros[k+1] = numeros[k]
            k -= 1
        numeros[k+1] = valor
    return numeros


# ---------------- SELECTION ----------------
def selection_nao_otimizado(numeros):
    arr = numeros[:]
    ordenados = []
    while arr:
        menor = min(arr)
        arr.remove(menor)
        ordenados.append(menor)
    return ordenados


def selection_otimizado(numeros):
    n = len(numeros)
    for i in range(n-1):
        menor = i
        for j in range(i+1, n):
            if numeros[j] < numeros[menor]:
                menor = j
        numeros[i], numeros[menor] = numeros[menor], numeros[i]
    return numeros


# ---------------- SHELL ----------------
def shell_nao_otimizado(numeros):
    gap = len(numeros) // 2
    while gap > 0:
        for i in range(gap, len(numeros)):
            temp = numeros[i]
            j = i
            while j >= gap and numeros[j-gap] > temp:
                numeros[j] = numeros[j-gap]
                j -= gap
            numeros[j] = temp
        gap //= 2
    return numeros


def shell_otimizado(numeros):
    gap = 1
    n = len(numeros)
    while gap < n // 3:
        gap = 3 * gap + 1
    while gap > 0:
        for i in range(gap, n):
            temp = numeros[i]
            j = i
            while j >= gap and numeros[j-gap] > temp:
                numeros[j] = numeros[j-gap]
                j -= gap
            numeros[j] = temp
        gap //= 3
    return numeros


# ---------------- MERGE ----------------
def merge_sort_basico(numeros):
    if len(numeros) <= 1:
        return numeros
    meio = len(numeros)//2
    esq = merge_sort_basico(numeros[:meio])
    dir = merge_sort_basico(numeros[meio:])
    return merge(esq, dir)


def merge_sort_otimizado(numeros):
    if len(numeros) <= 1:
        return numeros
    meio = len(numeros)//2
    esq = merge_sort_otimizado(numeros[:meio])
    dir = merge_sort_otimizado(numeros[meio:])
    if esq[-1] <= dir[0]:
        return esq + dir
    return merge(esq, dir)


def merge(esq, dir):
    resultado = []
    i = j = 0
    while i < len(esq) and j < len(dir):
        if esq[i] < dir[j]:
            resultado.append(esq[i]); i += 1
        else:
            resultado.append(dir[j]); j += 1
    resultado.extend(esq[i:])
    resultado.extend(dir[j:])
    return resultado


# ---------------- QUICK (CORRIGIDO) ----------------
def quick_sort_basico(numeros):
    if len(numeros) <= 1:
        return numeros

    pivo = numeros[len(numeros)//2]

    menores = [x for x in numeros if x < pivo]
    iguais = [x for x in numeros if x == pivo]
    maiores = [x for x in numeros if x > pivo]

    return quick_sort_basico(menores) + iguais + quick_sort_basico(maiores)


def quick_sort_otimizado(numeros, inicio=0, fim=None):
    if fim is None:
        fim = len(numeros) - 1
    if inicio < fim:
        p = particao(numeros, inicio, fim)
        quick_sort_otimizado(numeros, inicio, p-1)
        quick_sort_otimizado(numeros, p+1, fim)
    return numeros


def particao(arr, inicio, fim):
    pivo = arr[(inicio + fim)//2]
    while inicio <= fim:
        while arr[inicio] < pivo:
            inicio += 1
        while arr[fim] > pivo:
            fim -= 1
        if inicio <= fim:
            arr[inicio], arr[fim] = arr[fim], arr[inicio]
            inicio += 1
            fim -= 1
    return inicio - 1


# ---------------- HEAP ----------------
def heap_sort_basico(numeros):
    heapq.heapify(numeros)
    return [heapq.heappop(numeros) for _ in range(len(numeros))]


def heap_sort_otimizado(numeros):
    n = len(numeros)
    for i in range(n//2 - 1, -1, -1):
        heapify(numeros, n, i)
    for i in range(n-1, 0, -1):
        numeros[0], numeros[i] = numeros[i], numeros[0]
        heapify(numeros, i, 0)
    return numeros


def heapify(arr, n, i):
    maior = i
    esq = 2*i + 1
    dir = 2*i + 2
    if esq < n and arr[esq] > arr[maior]:
        maior = esq
    if dir < n and arr[dir] > arr[maior]:
        maior = dir
    if maior != i:
        arr[i], arr[maior] = arr[maior], arr[i]
        heapify(arr, n, maior)


# ---------------- LINEARES ----------------
def counting_sort(numeros):
    max_val = max(numeros)
    cont = [0]*(max_val+1)
    for n in numeros:
        cont[n] += 1
    resultado = []
    for i in range(len(cont)):
        resultado.extend([i]*cont[i])
    return resultado


def radix_sort(numeros):
    exp = 1
    max_val = max(numeros)
    while max_val // exp > 0:
        numeros = counting_digito(numeros, exp)
        exp *= 10
    return numeros


def counting_digito(numeros, exp):
    n = len(numeros)
    saida = [0]*n
    cont = [0]*10

    for num in numeros:
        cont[(num//exp)%10] += 1

    for i in range(1, 10):
        cont[i] += cont[i-1]

    for i in range(n-1, -1, -1):
        idx = (numeros[i]//exp)%10
        saida[cont[idx]-1] = numeros[i]
        cont[idx] -= 1

    return saida


def bucket_sort(numeros):
    buckets = [[] for _ in range(10)]
    max_val = max(numeros)

    for num in numeros:
        idx = num * 10 // (max_val + 1)
        buckets[idx].append(num)

    resultado = []
    for b in buckets:
        resultado.extend(sorted(b))
    return resultado


# ---------------- MEDIÇÃO ----------------
def medir(func, lista):
    return timeit.timeit(lambda: func(lista[:]), number=3) / 3


# ---------------- TESTE ----------------
random.seed(2026)
n = 5000

lista = gerador_aleatorio(1, 20000, n)
ordenada = sorted(lista)
inversa = sorted(lista, reverse=True)

algoritmos = [
    ("Bubble", bubble_nao_otimizado, bubble_otimizado),
    ("Insertion", insercao_nao_otimizado, insercao_otimizado),
    ("Selection", selection_nao_otimizado, selection_otimizado),
    ("Shell", shell_nao_otimizado, shell_otimizado),
    ("Merge", merge_sort_basico, merge_sort_otimizado),
    ("Quick", quick_sort_basico, quick_sort_otimizado),
    ("Heap", heap_sort_basico, heap_sort_otimizado),
]

extras = [
    ("Counting", counting_sort),
    ("Radix", radix_sort),
    ("Bucket", bucket_sort),
]

print("\nTrabalho de Classificação e Pesquisa de Dados\n")
print(" \nNome do Aluno: Eduardo Rafael da Silva Suarez\n")
print("")
print(f"{'Algoritmo':<20} {'Tipo':<12} {'Aleatória':<12} {'Ordenada':<12} {'Inversa':<12}")
print("-"*75)

for nome, nao, ot in algoritmos:
    print(f"{nome:<20} {'Normal':<12} {medir(nao, lista):.4f} {medir(nao, ordenada):.4f} {medir(nao, inversa):.4f}")
    print(f"{nome:<20} {'Otimizado':<12} {medir(ot, lista):.4f} {medir(ot, ordenada):.4f} {medir(ot, inversa):.4f}")
    print("-"*75)

for nome, func in extras:
    print(f"{nome:<20} {'Único':<12} {medir(func, lista):.4f} {medir(func, ordenada):.4f} {medir(func, inversa):.4f}")
    print("-"*75)
