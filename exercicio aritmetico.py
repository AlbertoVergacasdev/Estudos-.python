#Crie um algoritmo que leia um numero e mostre o seu dobro,triplo e raiz quadrada!
n = int(input('Digite um numero:'))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O dobro de {} vale {}.'.format(n, d))
print('O triplo de {} vale {}. \nA raiz Quadrada de {} e igual a {:.2f}.'.format(n, t,n, r))


#Tambem pode ser feito desse outro jeito:
#n = int(input('Digite um numero:'))
#print('O dobro de {} vale {}.'.format(n, (n*2)))
#print('O tripo de {} vale {}. \nA raiz quadrada de {} e igual {:.2f}.'.format(n, (n*3), n, pow(n, (1/2)))