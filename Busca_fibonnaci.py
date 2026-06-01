import random
def busca_fibonacci(arr,chave):

    n =  len(arr)

    fib2 = 0
    fib1 = 1
    fib = fib1 + fib2

    while fib < n :
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2


    offset = -1

    while fib > 1:

        i = min(offset + fib2, n - 1)

        if arr[i] < chave:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i

        elif arr[i] < chave:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i

        elif arr[i] > chave:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1

        else:
            return i
        
    if fib1 and offset + 1 < n and arr[offset + 1] == chave:
        return offset + 1
    
    return "inexistente"



random.seed(2025)

random_numbers = [random.randint(10, 50) for _ in range(10)]

print("Vetor original:")
print(random_numbers)

print("\nVetor ordenado:")
vetor_ordenado = sorted(random_numbers)
print(vetor_ordenado)


resultado = busca_fibonacci(vetor_ordenado, 33)

print("\nResultado da busca:")
print(resultado)
