#mouse
#variaveis
contador_total = 0
contador_sit1 = 0
contador_sit2 = 0
contador_sit3 = 0
contador_sit4 = 0
#entrada
indentificador = int(input("Informe a identificação: "))
#processamento/entrada
while indentificador != 0:
    print("1 - Necessidade de esfera. ")
    print("2 - Necessidade de limpeza. ")
    print("3 - Necessidade de troca do cabo ou conector. ")
    print("4 - Quebrado ou inutilizado. ")
    #entrada
    defeito = int(input("Informe o tipo de defeito: "))
    #processamento
    if defeito == 1:
        contador_sit1 = contador_sit1 + 1
    elif defeito == 2:
        contador_sit2 = contador_sit2 + 1
    elif defeito == 3:
        contador_sit3 = contador_sit3 + 1
    elif defeito == 4:
        contador_sit4 = contador_sit4 + 1
    contador_total = contador_total + 1
    indentificador = int(input("Informe a identificação: "))
p1 = contador_sit1 / contador_total * 100.0
p2 = contador_sit2 / contador_total * 100.0 
p3 = contador_sit3 / contador_total * 100.0 
p4 = contador_sit4 / contador_total * 100.0
print("Total de mouses: {0}".format(contador_total))
print("Situação                    Quantidade    Percentual")
print("1-Necessidade de esfera.        {0}          {1:.2f}%".format(contador_sit1,p1))
print("2-Necessidade de limpeza.       {0}          {1:.2f}%".format(contador_sit2,p2))
print("3-Necessidade de troca de cabo ou conector.       {0}          {1:.2f}%".format(contador_sit3,p3))
print("4-Quebrado ou inutilizado.        {0}          {1:.2f}%".format(contador_sit4,p4))