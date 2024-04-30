#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media
n1 = float(input('Primeira nota do aluno: '))
n2 = float(input('A segunda nota do aluno: '))
m = (n1 + n2) / 2
print('A media entre {:.1f} e {:.1f} e igual a {:.1f}'.format(n1, n2, m))