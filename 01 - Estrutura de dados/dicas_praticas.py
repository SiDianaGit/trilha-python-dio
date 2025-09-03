#🔹 1. Listas (list)

#List Comprehension:

quadrados = [x**2 for x in range(5)]
print(quadrados)  # [0, 1, 4, 9, 16]


#Desempacotar valores:

a, b, *resto = [1, 2, 3, 4, 5]
print(a, b, resto) # 1 2 [3, 4, 5]


#🔹 2. Dicionários (dict)

#Criar dicionário a partir de listas:

chaves = ["nome", "idade"]
valores = ["Ana", 25]
pessoa = dict(zip(chaves, valores))
print(pessoa) # {'nome': 'Ana', 'idade': 25}


#Iterar facilmente:

for chave, valor in pessoa.items():
  print(chave, "->", valor)


#🔹 3. Conjuntos (set)

# Remover duplicados de uma lista:

lista = [1, 2, 2, 3, 3, 4]
sem_duplicados = list(set(lista))
print(sem_duplicados) # [1, 2, 3, 4]


# Operações matemáticas úteis:

a = {1, 2, 3}
b = {3, 4, 5}
print(a & b) # interseção -> {3}
print(a | b) # união -> {1, 2, 3, 4, 5}


#🔹 4. Tuplas (tuple)

# Úteis para dados imutáveis:

ponto = (10, 20)
x, y = ponto
print(f"x={x}, y={y}")


# 5. Truque bônus – collections

# Contar elementos facilmente com Counter:

from collections import Counter
frutas = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
print(Counter(frutas))  
# Counter({'maçã': 3, 'banana': 2, 'laranja': 1})
