# 11. Dada uma lista com as notas de todos os alunos de uma turma, retorne a quantidade de alunos acima da média, que é 5

notas = [int(x) for x in input().split()]

acima_media = [nota for nota in notas if nota > 5]

aprovados = len(acima_media)

print(aprovados)
