#fazer um algoritmo que leia a variavel 'p'(peso de peixes) e verifique se há excesso.
#se houver, gravar na variavel 'e' (excesso) e na variavel 'm' o valor da multa que João deverá pagar. 
# caso contrário mostrar tais variaveis com o conteudo 'zero'.

#entradas
p = float(input("Informe o peso dos peixes: "))
#processamento
if p > 50:
    m = (p - 50) * 4.00
    e = 'excesso'
    print("Voce devera pagar R$ {0:.2f}".format(m))
else:
    m = 0
    e = 0
    print("Multas: {0}".format(m))
    print("Excesso: {0}".format(e))