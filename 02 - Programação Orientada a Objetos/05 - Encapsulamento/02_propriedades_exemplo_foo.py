class Foo:
    def __init__(self, x=None):
        self._x = x
    
    # depurador, é uma função que executa antes de tudo
    @property
    def x(self):
        #convencao de nome de atributo privado. Não deve ser chamado fora do escopo da classe
        return self._x or 0

    #modificar o valor de x. Trabalhar como um atributo. Não utilizar o return
    @x.setter
    def x(self, value):
        self._x += value

    #destruir a instancia
    @x.deleter
    def x(self):
        self._x = 0


foo = Foo(10)
print(foo.x)

del foo.x
print(foo.x)

foo.x = 100
print(foo.x)
