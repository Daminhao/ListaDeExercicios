#Tendo como dado de entrada a altura (h) de uma pessoa,
#construa um algoritmo que calcule seu peso ideal,
#utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

gen = int(input("Digite 1 para homem ou 2 para mulher:"))

if gen == 1:
    h = float(input('Digite sua altura:'))
    h2 = h * 72.7 - 58
    print(h2)
elif gen == 2:
    h = float(input("Digite sua altura:"))
    h2 = h * 62.1 - 44.7
    print(h2)
