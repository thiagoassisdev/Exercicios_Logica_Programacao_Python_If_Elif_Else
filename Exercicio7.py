ano = int(input("Digite um ano (1000-2999): "))

# Verifica se o ano está dentro do intervalo desejado (1000-2999)
if 1000 <= ano <= 2999:
    # Verifica se o ano é bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        print(f"{ano} é um ano bissexto.")
    else:
        print(f"{ano} não é um ano bissexto.")
else:
    print("Ano fora do intervalo válido (1000-2999).")



