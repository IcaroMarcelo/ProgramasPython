#elaborar um algoritmo que leia as variaveis 'c' e 'n', respectivamente código e número de horas trabalhadas
#de um operário. Calcule o salário sabendo-se que ele ganha R$ 10,00 por hora. Quando o número de horas exceder
#a 50 calcule o excesso de pagamento armazenando-o na variavel 'e'. Caso contrário zerar tal variavel.
#a hora excedente de trabalho vale R$ 20,00. No final do processamento imprimir o salário total e o salário excedente.
from Secao03.Exercicio06 import salario

#variaveis
valor_hora = 10.00
valor_hora_excedente = 20.00
e = 0
#entradas
c = int(input("Informe o código: "))
n = float(input("Informe a quantidade de horas trabalhadas: "))
#processamentos
if n > 50:
    e = (n - 50) * valor_hora_excedente
    salario = (50 * valor_hora) + e
    print("Salário Total R$ {0:.2f}".format(salario))
    print("Salário excedente R$ {0:.2f}".format(e))
else:
    salario = (n * valor_hora)
    print("Salário Total R$ {0:.2f}".format(salario))
    print("Salário excedente R$ {0:.2f}".format(e))