# 1. Defina uma função que leia do teclado uma sequência de números inteiros dados em uma única linha. A função deve retornar uma lista contendo os números que estão na linha.

def lista_numerica():
  return [map(int, input().split())]

lista_numerica()
