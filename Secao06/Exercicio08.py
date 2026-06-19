#algoritmo que leia um numero inteiro e mostre uma mensagem indicando se este numero é par ou impar
#e se é positivo ou negativo.
from Secao06.Exercicio02 import numero

#entradas
n1 = int(input("Informe um numero: "))
#processamento
if numero % 2 == 0:
    if numero > 0:
        print("O numero {0} é par e positivo".format(numero))
    else:
        print("O numero {0 é par e negativo}".format(numero))
else:
    if numero > 0:
        print("O numero {0} é impar e positivo".format(numero))
    else:
        print("O numero {0} é ímpar e negativo.".format(numero))