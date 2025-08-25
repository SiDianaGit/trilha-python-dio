class Cachorro:
    # método construtor/inicializador. Sempre é executado no inicio para instanciar
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        #atributos
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    #método destrutorv"del". Destroi a instancia. Sempre é executado no final da execução. É menos usado pois o python tem a função garbage 
    def __del__(self):
        print("Removendo a instância da classe.")

    def falar(self):
        print("auau")


def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)


c = Cachorro("Chappie", "amarelo")
c.falar()

print("Ola mundo")

# forçar a destruição da instancia de um objeto
del c

print("Ola mundo")
print("Ola mundo")
print("Ola mundo")

# criar_cachorro()
