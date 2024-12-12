import calculadora as calc

def teste():
    assert calc.soma(2,5) == 7, "Erro na soma"

    assert calc.subtracao(2) == 5, "Erro na subtração com memória"

    assert calc.soma(2,1) == 3, "Erro na soma"

