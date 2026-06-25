#algoritmo de indice de poluição medido e emitir a notificação adequada aos diferentes grupos de empresa.

#entradas
indice = float(input("Informe o índice de poluição: "))
#processamentos
if indice >= 0.3 and indice < 0.4:
    print("Atenção: Indústrias do 1o grupo devem suspender as atividades.")
elif indice >= 0.4 and indice < 0.5:
    print("Atenção: Indústrias do 2o grupo devem suspender as atividades.")
elif indice >= 0.5:
    print("Atenção: Todos os grupos devem suspender as atividades.")
