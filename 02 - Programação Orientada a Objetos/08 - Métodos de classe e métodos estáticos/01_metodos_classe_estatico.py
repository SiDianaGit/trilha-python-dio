class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    #depurador que transforma a instancia para metodo de classe. Onde cls é a referencia para a classe. Precisa do contexto da classe
    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2022 - ano
        return cls(nome, idade)

    #metodo estatico, não precisa do contexto da classe
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18

# chamando um metodo de classe
p = Pessoa.criar_de_data_nascimento(1994, 3, 21, "Guilherme")
print(p.nome, p.idade)

# chamando um metodo estatico
print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
