soma = lambda operando_a, operando_b: (operando_a + operando_b)

print(soma(2,2))
print(soma(4,2))
print(soma(5,2))

par_impar = lambda numero: True if numero % 2 == 0 else False

print(par_impar(2))
print(par_impar(3))

numeros = [1,2,3]

quadrado = list(map(lambda numero: numero**2, numeros))

print(quadrado)

'''maiuscula = map(lambda letra: letra.upper(), "ovo")

print("".join(maiuscula))'''

cel_far = lambda celsius: celsius * (9/5) + 32
arredonda = lambda valor: round(valor)
cel_far_arredonda = lambda celsius: arredonda(cel_far(celsius))
lista_cel = [1,2,3] 


x = list(map(cel_far_arredonda, lista_cel))
print(x)



