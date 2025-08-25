class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando o motor")

    #exibir a instancia/objeto
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

#classe Motocicleta é filha da clase Veiculo
class Motocicleta(Veiculo):
    pass

#classe Carro é filha da clase Veiculo
class Carro(Veiculo):
    pass

#classe Caminhão é filha da clase Veiculo
class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado):
        #o metodo super() traz as caractisticas do objeto pai, pois ao explicitar os atributos os mesmos foram sobrepostos
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} estou carregado")


moto = Motocicleta("preta", "abc-1234", 2)
carro = Carro("branco", "xde-0098", 4)
caminhao = Caminhao("roxo", "gfd-8712", 8, True)

print(moto)
print(carro)
print(caminhao)
