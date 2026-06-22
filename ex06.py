# 6. Contar quantidade de vogais em uma string

vogais = ['a', 'e', 'i', 'o', 'u']

strg = input().lower()
qtd_vogais = [vogal for vogal in strg if vogal in vogais]

print(len(qtd_vogais))
