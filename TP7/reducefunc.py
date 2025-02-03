from functools import reduce

lista = [2,100,4,0, 40]

x = lambda a,b: a*b

y = reduce(x, lista)

print(y)

z = lambda a,b: a if a > b else b

y = reduce(z, lista)

print(y)

tuplas = [("a", 1), ("b", 2), ("a", 3)]


