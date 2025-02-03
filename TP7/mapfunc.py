import math

lista = ["python", "lambda", "map"]

x = list(map(lambda palavra: palavra.upper(), lista))
print(x)

numeros = [4, 9, 25]

y = list(map(lambda numero: math.sqrt(numero), numeros))
print(y)

lista = ["Python é incrível", "Lambda são úteis", "Map é funcional"]


x = lambda frase: len(frase) 
y = lambda frase: len(frase.split())
z = lambda frase: {"palavras": y(frase), "caracteres": x(frase)}

print(list(map(z, lista)))




