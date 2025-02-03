def pares():
    for i in range(1,51):
        if i % 2 == 0:
            yield i

for i in pares():
    print(i)


def quadrado():
    c = 0
    for i in range(1,11):
        c += i**2
    print(c)

quadrado()

#outra forma

soma_quadrados = sum(i** 2 for i in range(1,11))
print(soma_quadrados)

def fib():
    a,b = 0,1
    while True:
        yield b
        a,b = b, a + b

fib = fib()
for i in range(0,11):
    print(next(fib))

def eh_primo(n):
    if n < 2:
        return False
    # Verifica se algum número entre 2 e sqrt(n) divide n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primos(start, end):
    for i in range(start, end + 1):
        if eh_primo(i) is True:
            yield i

for i in primos(10, 50):
    print(i)    


def fib_limitado(limite):
    a,b = 0,1
    while b <= limite:
        yield b 
        a,b = b, a + b

for i in fib_limitado(11):
    print(i)