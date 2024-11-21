class Conta:
    def __init__(self, numero:str):
        self.__numero = numero
        self.__saldo = 0.0
    def creditar(self, valor:float) -> None:
        self.__saldo += valor
    def debitar(self, valor:float) -> None:
        self.__saldo -= valor
    def get_numero(self) -> str:
        return self.__numero
    def get_saldo(self) -> float:
        return self.__saldo

class Banco:
    def __init__(self, taxa: float = 0.01):
        self.__contas = []
        self.__taxa = taxa

    def cadastrar(self, conta: Conta):
        self.__contas.append(conta)
    
    def procurar (self, numero:str)->Conta:
        for conta in self.__contas:
            if conta.get_numero() == numero:
                return conta
        return None
    
    def creditar(self, numero:str, valor:float)->None:
        conta = self.procurar(numero)
        if conta is not None:
            conta.creditar(valor)

    def debitar(self, numero:str, valor:float)->None:
        conta = self.procurar(numero)
        if conta is not None:
            conta.debitar(valor)
    
    def saldo(self,numero:str)->float:
        conta = self.procurar(numero)
        if conta is not None:
            return conta.get_saldo()
        
    def render_juros(self, numero:str) -> None:
        conta = self.procurar(numero)
        if isinstance(conta, ContaPoupanca):
            conta.render_juros(self.__taxa)

    def get_taxa(self) -> float:
        return self.__taxa

    def set_taxa(self, taxa:float) -> None:
        self.__taxa = taxa
    
    def render_bonus(self, numero:str) -> None:
        conta = self.procurar(numero)
        if isinstance(conta, ContaEspecial):
            conta.render_bonus()

    def transferir(self, origem:str, destino:str, valor:float)->None:
        conta_origem = self.procurar(origem)
        conta_destino = self.procurar(destino)
        if conta_origem and conta_destino is not None:
            conta_origem.debitar(valor)
            conta_destino.creditar(valor)

class ContaPoupanca(Conta):
    def __init__(self, numero:str):
        super().__init__(numero)
    def render_juros(self, taxa:float) -> None:
        self.creditar(self.get_saldo() * taxa)

class ContaEspecial(Conta):
    def __init__(self, numero:str):
        super().__init__(numero)
        self.__bonus = 0
    def render_bonus(self) -> None:
        self.creditar(self.__bonus)
        self.__bonus = 0
    def creditar(self, valor:float) -> None:
        self.__bonus += valor * 0.01
        super().creditar(valor)

