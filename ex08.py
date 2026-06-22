# 8. Faça uma lista com os números pares de uma lista de inteiros

nums = input().split()

num_par = [int(n) for n in nums if int(n) % 2 == 0]

print(num_par)
