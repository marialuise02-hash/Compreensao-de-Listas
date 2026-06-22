# 12. Crie uma lista que que extraia todas as letras das palavras e gere uma única lista. Ex: palavras = ["python", "java"]. Saída = ['p', 'y', 't', 'h', 'o', 'n', 'j', 'a', 'v', 'a']

texto = input().split()

lista = [letra for letra in linha for linha in texto]

print(lista)
