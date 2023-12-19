#Um estacionamento cobra R$ 5,00 por hora porém possui
# um teto de cobrança máxima de R$ 35,00, independente do número de horas.
# Escreva um algoritmo que pergunte ao usuário qual foi o período de permanência
# em horas e escreva na tela o total a pagar.

num= int(input("Informe o periodo de permanência:"))

valor = num*5

if valor<=35:
    print(f"Você deve pagar o valor de R$: {valor:.2f}")

elif valor>=35:
    print(f"total a pagar é de R$35,00")