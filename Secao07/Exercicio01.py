#algoritmo que determine o maior entre N numeros. A condição de parada é a entrada de um valor 0,ou seja,
#o algoritmo deve ficar calculando o maior até que a entrada seja igual a 0(ZERO).

#variaveis
maior = 0

#entrada
n = int(input("Informe um número: "))
while n != 0:
    if n > maior:
        maior = n
    n = int(input("Informe um número: "))
print("O maior numero é {0}".format(maior))