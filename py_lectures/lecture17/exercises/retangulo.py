class Retangulo:
    """
    esta classe cria um retangulo que implementa como atributos(caracteristicas) - base e altura 
    tambem permite como metodos(ações) - mudar os valores da base e altura, juntamente a isso calcular 
    area e perimetro com os novos valores.
    """
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def mudar_valores(self, n_base, n_altura):
        self.n_base = n_base
        self.n_altura = n_altura
    def calc_area(self):
        area = (self.n_base * self.n_altura)
        return f"a area é de {area}m²"
    def calc_perimetro(self):
        perimetro = (self.n_base * 2) + (self.n_altura * 2)
        return f"o perímetro é igual a {perimetro}m"

retangulo = Retangulo(20, 30)
retangulo.mudar_valores(2, 3)
# é o mesmo que
# retangulo.n_base = 2
# retangulo.n_altura = 3

print(retangulo.calc_area())
print(retangulo.calc_perimetro())


