import random
import timeit

# ---------------- GERADOR ----------------
def gerador_aleatorio(inicial, final, numeros):
    numeros_aleatorios = []
    for _ in range(numeros):
        numeros_aleatorios.append(random.randint(inicial, final))
    return numeros_aleatorios


# ---------------- BUBBLE ----------------
def bubble_nao_otimizado(numeros):
    n = len(numeros) - 1
    for i in range(n):
        k = 0
        while k < n:
            if numeros[k] > numeros[k+1]:
                numeros[k], numeros[k+1] = numeros[k+1], numeros[k]
            k += 1
    return numeros


def bubble_otimizado(numeros):
    n = len(numeros) - 1
    for i in range(n-1):
        k = 0
        while k < n - i:
            if numeros[k] > numeros[k+1]:
                numeros[k], numeros[k+1] = numeros[k+1], numeros[k]
            k += 1
    return numeros


# ---------------- INSERTION ----------------
def insercao_nao_otimizado(numeros):
    for i in range(1, len(numeros)):
        k = 0
        while k < i:
            if numeros[i] < numeros[k]:
                numeros.insert(k, numeros.pop(i))
                break
            k += 1
    return numeros


def insercao_otimizado(numeros):
    for i in range(1, len(numeros)):
        k = i - 1
        valor = numeros[i]
        while k >= 0 and valor < numeros[k]:
            numeros[k+1] = numeros[k]
            k -= 1
        numeros[k+1] = valor
    return numeros


# ---------------- SELECTION ----------------
def selection_nao_otimizado(numeros):
    arr = numeros[:]
    ordenados = []
    while len(arr) > 0:
        menor = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[menor]:
                menor = i
        ordenados.append(arr.pop(menor))
    return ordenados


def selection_otimizado(numeros):
    n = len(numeros)
    for j in range(n-1):
        menor = j
        for i in range(j+1, n):
            if numeros[i] < numeros[menor]:
                menor = i
        numeros[j], numeros[menor] = numeros[menor], numeros[j]
    return numeros


# ---------------- SHELL SORT ----------------
def shell_nao_otimizado(numeros):
    n = len(numeros)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = numeros[i]
            j = i
            while j >= gap and numeros[j - gap] > temp:
                numeros[j] = numeros[j - gap]
                j -= gap
            numeros[j] = temp
        gap //= 2

    return numeros


def shell_otimizado(numeros):
    n = len(numeros)
    gap = 1

    while gap < n // 3:
        gap = 3 * gap + 1

    while gap > 0:
        for i in range(gap, n):
            temp = numeros[i]
            j = i
            while j >= gap and numeros[j - gap] > temp:
                numeros[j] = numeros[j - gap]
                j -= gap
            numeros[j] = temp
        gap //= 3

    return numeros


# ---------------- MEDIÇÃO ----------------
def medir_tempo(func, lista):
    return timeit.timeit(
        lambda: func(lista[:]),
        number=3
    ) / 3


# ---------------- TESTES ----------------
random.seed(2026)

n = 10000

lista_aleatoria = gerador_aleatorio(1, 20000, n)
lista_ordenada = sorted(lista_aleatoria)
lista_inversa = sorted(lista_aleatoria, reverse=True)

resultados = []

# Bubble
resultados.append(("Bubble (não otimizado)",
    medir_tempo(bubble_nao_otimizado, lista_aleatoria),
    medir_tempo(bubble_nao_otimizado, lista_ordenada),
    medir_tempo(bubble_nao_otimizado, lista_inversa)
))

resultados.append(("Bubble (otimizado)",
    medir_tempo(bubble_otimizado, lista_aleatoria),
    medir_tempo(bubble_otimizado, lista_ordenada),
    medir_tempo(bubble_otimizado, lista_inversa)
))

# Insertion
resultados.append(("Insertion (não otimizado)",
    medir_tempo(insercao_nao_otimizado, lista_aleatoria),
    medir_tempo(insercao_nao_otimizado, lista_ordenada),
    medir_tempo(insercao_nao_otimizado, lista_inversa)
))

resultados.append(("Insertion (otimizado)",
    medir_tempo(insercao_otimizado, lista_aleatoria),
    medir_tempo(insercao_otimizado, lista_ordenada),
    medir_tempo(insercao_otimizado, lista_inversa)
))

# Selection
resultados.append(("Selection (não otimizado)",
    medir_tempo(selection_nao_otimizado, lista_aleatoria),
    medir_tempo(selection_nao_otimizado, lista_ordenada),
    medir_tempo(selection_nao_otimizado, lista_inversa)
))

resultados.append(("Selection (otimizado)",
    medir_tempo(selection_otimizado, lista_aleatoria),
    medir_tempo(selection_otimizado, lista_ordenada),
    medir_tempo(selection_otimizado, lista_inversa)
))

# Shell
resultados.append(("Shell (não otimizado)",
    medir_tempo(shell_nao_otimizado, lista_aleatoria),
    medir_tempo(shell_nao_otimizado, lista_ordenada),
    medir_tempo(shell_nao_otimizado, lista_inversa)
))

resultados.append(("Shell (otimizado)",
    medir_tempo(shell_otimizado, lista_aleatoria),
    medir_tempo(shell_otimizado, lista_ordenada),
    medir_tempo(shell_otimizado, lista_inversa)
))


# ---------------- PRINT FINAL ----------------
print("\nTrabalho de Classificação e Pesquisa de Dados")
print("Aluno: Eduardo Rafael da Silva Suarez\n")

print(f"{'Método':<30} {'Aleatória':<15} {'Ordenada':<15} {'Inversa':<15} {'Melhora (%)':<15}")
print("-" * 95)

for i in range(0, len(resultados), 2):
    nome_nao, ale_nao, ord_nao, inv_nao = resultados[i]
    nome_ot, ale_ot, ord_ot, inv_ot = resultados[i+1]

    tempo_nao = (ale_nao + ord_nao + inv_nao) / 3
    tempo_ot = (ale_ot + ord_ot + inv_ot) / 3

    if tempo_nao > 0:
        melhora = ((tempo_nao - tempo_ot) / tempo_nao) * 100
    else:
        melhora = 0

    print(f"{nome_nao:<30} {ale_nao:.4f}s{'':<8} {ord_nao:.4f}s{'':<8} {inv_nao:.4f}s")
    print(f"{nome_ot:<30} {ale_ot:.4f}s{'':<8} {ord_ot:.4f}s{'':<8} {inv_ot:.4f}s{'':<5} {melhora:.2f}%")
    print("-" * 95)
