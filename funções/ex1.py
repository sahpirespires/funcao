def area(largura, comprimento):
    area_terreno = largura * comprimento
    return area_terreno

largura = float(input("Digite a largura do terreno: "))
comprimento = float(input("Digite o comprimento do terreno: "))

area_terreno = area(largura, comprimento)

print("A área do terreno é:", area_terreno, "metros quadrados.")

