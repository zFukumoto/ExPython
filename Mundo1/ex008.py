# Escreva um programa que leia um valor em metros e a exiba convertido em centímeros e milímetros
m = float(input('Digite um valor em metros:'))
km = m/1000
hm = m/100
dam = m/10
dm = m*10
cm = m*100
mm = m*1000
print(m,'m equivale a:')
print(km,'km')
print(hm,'hm')
print(dam,'dam')
print(dm,'dm')
print(cm,'cm')
print(mm,'mm')
