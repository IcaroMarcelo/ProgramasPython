#fazer um algoritmo para calcular o estoque medio de uma peça
#sendo que: estoque_medio = (quantidade_minima + quantidade_maxima) / 2
#entrada
quantidade_minima = int(input("Informe a quantidade mínima: "))
quantidade_maxima = int(input("Informe a quantidade maxima: "))
#processamento
estoque_medio = (quantidade_minima + quantidade_maxima) / 2
#saida
print("O estoque médio é {0}".format(estoque_medio))