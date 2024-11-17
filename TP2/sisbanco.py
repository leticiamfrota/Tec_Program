class Conta:
    def __init__(self, numero:str):
        pass
    def creditar(self, valor:float) -> None:
        pass
    def debitar(self, valor:float) -> None:
        pass
    def get_numero(self) -> str:
        pass
    def get_saldo(self) -> float:
        pass

class Banco:
    def __init__(self):
        pass

    def cadastrar(self, conta: Conta):
        pass
    
    def procurar (self, numero:str)->Conta:
        pass
    
    def creditar(self, numero:str, valor:float)->None:
        pass 

    def debitar(self, numero:str, valor:float)->None:
        pass
    
    def saldo(self,numero:str)->float:
        pass

    def transferir(self, origem:str, destino:str, valor:float)->None:
        pass