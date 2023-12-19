#As maçãs custam R$ 1,30 cada se forem compradas menos de uma dúzia,
#e R$ 1,00 se forem compradas pelo menos 12. Escreva um programa que leia o
#número de maçãs compradas, calcule e escreva o custo total da compra.

mac = int(input("Informe a quantidade de maças compradas:"))

if mac<=5:
   mac2=mac*1.30
   print(f"O valor total da compra é R$:{mac2:.2f}")

elif mac>=12:
    mac3=mac*1
    print(f"O valor total da compra é R$:{mac3:.2f}")

else:
    print(f"O valor total da compra é R$:{mac:.2f}")