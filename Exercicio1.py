#Escreva um algoritmo que pergunte o valor de uma mercadoria e qual o valor que o usuário tem em
#mãos e diga se o dinheiro é ou não é suficiente para adquirir esta mercadoria;

num1= int(input("Informe o valor da mercadoria:"))
num2= int(input("Informe o valor que o usuario tem em mãos:"))


if num1>num2:
    print("Você não tem dinheiro o suficiente para comprar a mercadoria.")

else:
    print("Você tem dinheiro o suficiente para comprar a mercadoria.")
