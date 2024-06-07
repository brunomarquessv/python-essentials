class Pessoa(object):
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    def envelhecer(self):
        self.nova_idade = self.idade + 1
        return self.nova_idade
    def crescer(self):
        if self.nova_idade > 21:
            self.altura += 0.005
        return self.altura
    def engordar(self):
        if self.nova_idade > self.idade:
            self.peso += 1
        return f"voce engordou! seu novo peso é de {self.peso}kg"
    
   

    
pessoa = Pessoa("Bruno", 22, 73, 1.84)
print(pessoa.nome, pessoa.idade, pessoa.peso, pessoa.altura)
print(pessoa.envelhecer())
print(pessoa.crescer())
print(pessoa.engordar())

        
