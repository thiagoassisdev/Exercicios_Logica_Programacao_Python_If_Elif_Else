#Uma livraria resolveu fazer uma promoção, com os seguintes critérios:
#o	Livros com preços até R$ 10,00 - desconto de 8%
#o	Livros com preços de R$ 10,01 até R$ 60,00 - desconto de 10%
#o	Livros com preços acima de R$ 60,00 - desconto de 20%
#Escreva um algoritmo que leia o preço do livro e mostre o valor do desconto
# oferecido, em reais.

preco_livro = float(input("Digite o preço do livro: R$ "))

# Inicializa a variável de desconto como 0
desconto = 0

# Aplica as regras de desconto com base no preço do livro
if preco_livro <= 10.00:
    desconto = preco_livro * 0.08
elif 10.01 <= preco_livro <= 60.00:
    desconto = preco_livro * 0.10
else:
    desconto = preco_livro * 0.20

# Exibe o valor do desconto em reais
print(f"O valor do desconto é de R$ {desconto:.2f}")
