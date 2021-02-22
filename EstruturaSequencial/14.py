# Multa por excesso
peso = float(input('Digite o peso dos peixes:'))

if peso < float(50):
    print("Ta safe")

elif peso > float(50):
    excesso = peso - float(50)
    multa = excesso * 4
    print('Malandro vai ter que pagar:', multa, 'de multa.')