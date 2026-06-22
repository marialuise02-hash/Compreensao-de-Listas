# 8. Faça uma lista com os números pares de uma lista de inteiros

nums = input().split()

num_par = [n for n in nums if n%2 == 0]

print(num_par)
