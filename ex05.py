# 5. Dada uma lista com nomes, filtrar palavras maiores que 5 letras

nomes = input().split()
nomes_filtrados = [nome for i in nomes if len(i) > 5]

print(nomes_filtrados)
