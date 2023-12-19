#Escreva um programa que pergunte ao usuário qual foi a média anual de
# um aluno  e ao final diga se ele está aprovado, reprovado ou de exame.
# Considere que o aluno está aprovado caso a média seja maior ou igual a 6.0;
# de exame com a média entre 3.0 e 5.9 e reprovado com média menor do que 3.0.

med = float(input("Informe a sua média atual:"))

if med>=6:
    print("Você foi aprovado!")

if med>=3 and med<=5.9:
    print("Você está de exame!")

elif med<=2.9:
    print("Você foi reprovado!")



