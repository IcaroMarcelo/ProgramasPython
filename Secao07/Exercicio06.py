#Gerador de tabuadas, capaz de gerar tabuada de qualquer numero inteiro entre 1 e 10.
#O usuario deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
#tabuada do 5:
#5 X 1 = 5
#5 X 2 = 10
#...

#entrada
numero = int(input("Informe um número entre 1 e 10: "))

#processamento
while numero < 1 or numero > 10:
    numero = int(input("Informe um numero entre 1 e 10: "))
print("Tabuada de {0}".format(numero))
for n in range(1,11):
    print("{0} X {1} = {2}".format(numero, n, (numero * n)))