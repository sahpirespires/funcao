def voto(ano):
    v = 2023 - ano
    if v >= 18:
        print("Voto obrigatório")
    elif v < 18 and v >= 16:
        print("Voto opcional")
    else:
        print("Voto negado")

A = int(input("Digite o ano de nascimento: "))
voto(A)