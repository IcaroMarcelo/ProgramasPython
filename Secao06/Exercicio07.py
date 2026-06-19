# um algoritmo que leia quatro numeros,calcule o quadrado de cada um
# se o valor resultante do quadrado do terceiro for >= 1000, imprima-o e finalize;
# caso contrario, imprima os valores lidos e seus respectivos quadrados.

#entradas
n1 = int(input("Informe o numero 1: "))
n2 = int(input("Informe o numero 2: "))
n3 = int(input("Informe o numero 3: "))
n4 = int(input("Informe o numero 4: "))
#processamento
q1= n1 * n1
q2= n2 * n2
q3= n3 * n3
q4= n4 * n4

if q3 >= 1000:
    print(q3)
else:
    print("Num1: {0}, Quadrado: {1}".format(n1,q1))
    print("Num2: {0}, Quadrado: {1}".format(n2,q2))
    print("Num3: {0}, Quadrado: {1}".format(n3,q3))
    print("Num4: {0}, Quadrado: {1}".format(n4,q4))
    
