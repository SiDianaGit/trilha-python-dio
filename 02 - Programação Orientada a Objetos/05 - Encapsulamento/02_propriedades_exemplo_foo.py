class Foo:
    def __init__(self, x=None):
        self._x = x

    @property
    def x(self):
        #convencao de nome de atributo privado. Não deve ser chamado fora do escopo
        return self._x or 0

    @x.setter
    def x(self, value):
        self._x += value

    @x.deleter
    def x(self):
        self._x = 0


foo = Foo(10)
print(foo.x)
del foo.x
print(foo.x)
foo.x = 10
print(foo.x)
