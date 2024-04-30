#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
medida = float(input('Uma Distancia em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m \ncorresponde a {:.0f}cm \ne {:.0f}mm'.format(medida, cm, mm))