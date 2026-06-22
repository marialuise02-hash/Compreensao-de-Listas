# 10. Dada uma lista numérica, retorne apenas os números positivos

nums = input().split()

nums_positivos = [num for num in nums if num > 0]

print(nums_positivos)
