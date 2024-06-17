class Bola():
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def troca_cor(self, nova_cor):
        self.cor = nova_cor
    
    def mostra_cor(self):
        return f"A cor da bola é {self.cor}"

minha_bola = Bola("vermelha", 20, "plástico")
print(minha_bola.mostra_cor())
minha_bola.troca_cor("azul")
print(minha_bola.mostra_cor())
