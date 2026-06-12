#Tendo como dados a altura e o sexo da pessoa, construa um algoritmo que calcule seu peso ideal,
#utilizando as seguintes fórmulas:
#para homens: (72.7 * altura) - 58
#para mulheres: (62.7 * altura) - 44.7


#entradas
altura = float(input("Informe sua altura please: "))
sexo = input("Informe o sexo m/f: ")
#processamento
if sexo.lower() == 'm':
    peso_ideal = (72.7 * altura) - 58
elif sexo.lower() == 'f':
    peso_ideal = (62.1 * altura) - 44.7
else:
    peso_ideal = 0
    print("Sexo não reconhecido.")
#saida
print("Seu peso ideal é {0:.2f}".format(peso_ideal))