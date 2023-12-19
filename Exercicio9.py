#Considerando o IMC (índice de massa corpórea), calculado como
# peso # /(altura*altura), exiba a situação da pessoa com base na seguinte tabela:
#IMC	Situação
#<= 18.5	Abaixo do peso
#>18.5 e <=24.9	Peso ideal
#>24.9	Acima do peso

peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

# Calcula o IMC (índice de massa corporal)
imc = peso / (altura * altura)

# Determina a situação da pessoa com base no IMC
if imc <= 18.5:
    situacao = "Abaixo do peso"
elif 18.5 < imc <= 24.9:
    situacao = "Peso ideal"
else:
    situacao = "Acima do peso"

# Exibe a situação da pessoa
print(f"Situação: {situacao}")



