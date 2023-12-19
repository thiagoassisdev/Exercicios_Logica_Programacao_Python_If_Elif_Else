#Escreva um algoritmo que verifique se um número inteiro
#digitado pelo usuário é ou não divisível por 5.

num = int(input("Informe o numero inteiro:"))


if (num % 5 == 0):
    print("O numero é divisivel por 5")

div = num % 5

if div  <=0:
    print("O valor é divisivel por 5!")

else:
    print("O valor não é divisivel por 5!")

