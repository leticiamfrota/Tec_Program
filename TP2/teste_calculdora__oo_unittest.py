from calculadora_oo import Calculadora
import unittest

class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.calc = Calculadora()

    def test_get_acumulador(self):
        self.assertEqual(self.calc.get_acumulador(), 0.0, "Inicialização Acumulador Incorreta")

    def test_soma(self):
        calc = Calculadora
        self.assertEqual(self.calc.soma(2,3), 5, "Erro na soma")



if __name__ == "__main__":
    unittest.main()