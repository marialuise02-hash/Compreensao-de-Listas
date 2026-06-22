# 2. Defina a função "descendentes" que pega uma árvore genealógica e retorna todos os descendentes da raiz. Utilize compreensões.

def descendentes(integrantes):
  integrantes = [input().split()]
  return integrantes[2:]

print(descendentes(integrantes))
