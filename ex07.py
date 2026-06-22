# 7. Gere uma lista contendo o tamanho de cada palavra. Ex de entrada: ["python", "java", "javascript", "c"]

entrada = [input().split()]

qtd_letras = [palavra for len(palavra) in entrada]

print(qtd_letras)
