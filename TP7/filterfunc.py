lista = [-10, 15, -20, 25, 0, 30]

z = lambda x: x > 0 
y = list(filter(z, lista))

print(y)

lista = ["Senhor", "Casa", "Teclado", "Uva"]

x = lambda palavra: len(palavra) > 5
y = list(filter(x, lista))
print(y)

lista = [-10, 15, -20, 25, 0, 30, 3]

x = lambda x: x % 3 == 0
y = lambda x: x % 5 == 0
z = lambda x: x > 0

c = lambda k: (x(k) or y(k)) and z(k)

k = list(filter(c, lista))
print(k)