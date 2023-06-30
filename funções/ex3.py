def maior(*valores):
    maior_valor = None
    for valor in valores:
        if maior_valor is None or valor > maior_valor:
            maior_valor = valor
    return maior_valor


resultado = maior(10, 5, 8, 15, 3)
print("O maior valor é:", resultado)
