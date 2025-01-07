from sisbanco import Conta, ContaAbstrata, Banco, ContaImposto, ContaPoupanca, ContaEspecial
import unittest

class TestConta(unittest.TestCase):
    def test_debitar(self):
        conta = Conta("123")
        conta.debitar(5)
        self.assertEqual(conta.get_saldo(), -5.0, "Erro no debitar")

        conta.creditar(10)
        conta.debitar(5)
        self.assertEqual(conta.get_saldo(), 0.0, "Erro no debitar")

    def test_creditar(self):
        conta = Conta("123")
        conta.creditar(5)
        self.assertEqual(conta.get_saldo(), 5.0, "Erro no creditar")

        conta.debitar(5)
        self.assertEqual(conta.get_saldo(), 0.0, "Erro no creditar")
    
    def test_get_numero(self):
        conta = Conta("123")
        self.assertEqual(conta.get_numero(), "123", "Erro no get_numero")
    
    def test_get_saldo(self):
        conta = Conta("123")
        self.assertEqual(conta.get_saldo(), 0.0, "Erro no get_saldo")
        conta.creditar(5)
        self.assertEqual(conta.get_saldo(), 5.0, "Erro no get_saldo")
        conta.debitar(2)
        self.assertEqual(conta.get_saldo(), 3.0, "Erro no get_saldo")
    
class TestContaPoupança(unittest.TestCase):
    def test_render_juros(self):
        conta = ContaPoupanca("123")
        conta.render_juros(0.01)
        self.assertEqual(conta.get_saldo(), 0.0, "Erro no render_juros")
        conta.creditar(10)
        conta.render_juros(0.01)
        self.assertEqual(conta.get_saldo(), 10 + (0.01 * 10), "Erro no render_juros")

class TestContaEspecial(unittest.TestCase):
    def test_render_bonus(self):
        conta = ContaEspecial("123")
        conta.render_bonus()
        self.assertEqual(conta.get_saldo(), 0.0, "Erro no render_bonus")
        conta.creditar(10)
        conta.render_bonus()
        self.assertEqual(conta.get_saldo(), 10 + (10 * 0.01), "Erro no render_bonus")
        conta.debitar(10 + (10 * 0.01))
        conta.creditar(5)
        conta.creditar(10)
        conta.render_bonus()
        self.assertEqual(conta.get_saldo(), 15 + (15 * 0.01), "Erro no render_bonus")

        
    def test_creditar(self):
        conta = ContaEspecial("123")
        conta.creditar(10)
        self.assertEqual(conta.get_saldo(), 10, "Erro no creditar")


if __name__ == "__main__":
    unittest.main()