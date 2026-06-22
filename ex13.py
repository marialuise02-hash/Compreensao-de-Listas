# 13. Dada uma matriz de inteiros, me faça uma lista com apenas os numeros pares da matriz

tamanho_matriz = int(input())

matriz = [[int(x) for i in input().split()] for i in range(tamanho_matriz)]

nums_pares = [num for linha in matriz for num in linha if num % 2 == 0]

print(nums_pares)
