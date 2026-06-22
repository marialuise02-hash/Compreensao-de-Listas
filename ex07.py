# 7. Gere uma lista contendo o tamanho de cada palavra. Ex de entrada: ["python", "java", "javascript", "c"]

entrada = input().split()

qtd_letras = [len(palavra) for palavra in entrada]

print(qtd_letras)
