#Fazer um algoritmo que pergunte o quanto voce ganha por hora e o número de horas trabalhadas no mes.
#Calcule e mostre o total do seu salário no referido mês.

#entrada
quant_horas_trabalhadas = int(input("Informe a quantidade de horas trabalhadas: "))
valor_hora = float(input("Infome o valor da hora."))
#processamento
salario = quant_horas_trabalhadas * valor_hora
#saida
print("o seu salario é de R${0:.2f}").format(salario)

