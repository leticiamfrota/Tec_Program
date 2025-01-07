def divisao_inteligente(func):
    def wrapper(x,y):
        print("Dividindo:{}/{}".format(x,y))
        if y == 0.0:
            return "ERRO_DIV_POR_ZERO"
        else:
            return func(x,y)
    
    return wrapper

@divisao_inteligente
def dividir(operando_a:float,operando_b:float):
    return operando_a/operando_b

print(dividir(3,1))
print(dividir(3,0))