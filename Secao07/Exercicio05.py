#fazer um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuario,
#mostrando uma mensagem de erro e voltando a pedir as informações.

#entradas
nome = input("Informe o nome: ")
senha = input("Informe a senha: ")
#processamento
while nome == senha:
    print("Nome de usuario e senha devem ser diferentes. ")
    nome = input("Informe o nome: ")
    senha = input("Informe a senha: ")