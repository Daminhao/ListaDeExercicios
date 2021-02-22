

timegain = float(input("Digite ganho por Hora:"))
timework = float(input("Horas trabalhadas"))
#Salario bruto
totalbruto =float(timegain * timework)

#Desconto no I.R
Ir = totalbruto * 0.11
inss = totalbruto * 0.08
sind = totalbruto * 0.05

des = Ir + inss + sind

salaliq =  totalbruto - des

#Resultado
print('Bruto total = R$:',totalbruto)
print('Imposto de renda = R$:',Ir)
print('INSS = R$:',inss)
print('Sindicato = R$:',sind)
print('Total de descontos = R$:',des)
print('Total Liquido = R$:',salaliq)



