#Elaborar um algoritmo que leia um numero. Se positivo armazene-o em 'a', se for negativo, em 'b'
#No final mostrar o resultado.

#entradas
numero = int(input("Informe um numero: "))
#processamento
if numero > 0: 
    a = numero
    print("valor positivo.")
else:
    b = numero
    print("valor negativo.")
print(numero)