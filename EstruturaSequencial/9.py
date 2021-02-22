#Faça um Programa que peça a temperatura em graus Fahrenheit
#transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).
#(0°F − 32) × 5/9 = -17.78°C

fah = float(input("Digite a temp em Fahrenheit:"))

result = fah - 32 * 5/9

print("Graus Celsious:", result)