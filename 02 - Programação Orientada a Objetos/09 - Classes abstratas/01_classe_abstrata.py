# Classe abstrata (ou Interface) não é instanciada. Não permite herança multipla. Serve para compor comportamentos. Não possui uma palavra reservada para interface.
# Módulo ABD (abstracted basic class)

from abc import ABC, abstractmethod, abstractproperty

# a classe pai não tem corpo em seus métodos.  E todas as classes filhas são obrigadas a ter uma definição em cada um de seus métodos replicados (neste caso os 2 metodos). Dá segurança para fazer polimorfirmos.
class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    #forçando a obrigatoriedade de propriedade dentro de cada classe filha
    @property
    @abstractproperty
    def marca(self):
        pass


class ControleTV(ControleRemoto):
    def ligar(self):
        print("Ligando a TV...")
        print("Ligada!")

    def desligar(self):
        print("Desligando a TV...")
        print("Desligada!")

    @property
    def marca(self):
        return "Philco"


class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print("Ligando o Ar Condicionado...")
        print("Ligado!")

    def desligar(self):
        print("Desligando o Ar Condicionado...")
        print("Desligado!")

    @property
    def marca(self):
        return "LG"


controle = ControleTV()
controle.ligar()
controle.desligar()
print(controle.marca)


controle = ControleArCondicionado()
controle.ligar()
controle.desligar()
print(controle.marca)
