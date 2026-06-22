# 10. Dada uma lista numérica, retorne apenas os números positivos

nums = [int(x) for x in input().split()]

nums_positivos = [num for num in nums if num > 0]

print(nums_positivos)
