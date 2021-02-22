#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

num1 = int(input())
num2 = int(input())

num3 = float(input())

result1 = num1 * 2 + num2/2

result2 = num1 * 3 + num3

result3 = num3**3

print('Seu resultado é:',result1, result2, result3)