class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    #Retornar os valores do objeto/instancia criada
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    # o valor "**kw" é o key argments, onde força a chamada por chave e valor, possibilitando o python utilizar os atributos da classe pai
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        # super recupera os atributos o objeto pai
        super().__init__(**kw)


class Ave(Animal):
    # o valor "**kw" é o key argments, onde força a chamada por chave e valor, possibilitando o python utilizar os atributos da classe pai
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)


class Gato(Mamifero):
    pass

class FalarMixin:
    def falar(self):
        print("oi estou falando")

class Ornitorrinco(Mamifero, Ave, FalarMixin):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        super().__init__(cor_pelo=cor_pelo, cor_bico=cor_bico, nro_patas=nro_patas)
        print(Ornitorrinco.__mro__)  # exibe a ordem que o python executou as classes
        print(Ornitorrinco.mro())


gato = Gato(nro_patas=4, cor_pelo="Preto")
print(gato)

ornitorrinco = Ornitorrinco(nro_patas=2, cor_pelo="vermelho", cor_bico="laranja")
print(ornitorrinco)
print(ornitorrinco.falar())
