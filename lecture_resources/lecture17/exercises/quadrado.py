class Quadrado():
    def __init__(self, lado):
        self.lado = lado
    def mudar_lado(self, novo_lado):
        self.novo_lado = novo_lado
    def mostrar_area(self):
        self.novo_lado = self.novo_lado
        area = self.novo_lado ** 2
        return f"a area é de {area}m²"


quadrado = Quadrado(5)
print(quadrado.lado)
quadrado.mudar_lado(7)
print(quadrado.novo_lado)
print(quadrado.mostrar_area())