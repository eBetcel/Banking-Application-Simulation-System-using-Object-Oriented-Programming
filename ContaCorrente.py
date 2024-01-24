from Conta import Conta


class ContaCorrente(Conta):
    def __init__(self, clientes, numero, agencia, saldo):
        super().__init__()
        self._clientes = clientes
        self._numero = numero
        self._agencia = agencia
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo

    def consultar_saldo(self):
        return self.saldo

    def creditar(self, valor):
        try:
            valor = float(valor)
            if valor <= 0:
                raise ValueError("Valor menor que zero")
            self._saldo += valor
        except:
            raise ValueError("Valor inválido")


    def debitar(self, valor):
        try:
            valor = float(valor)
            if valor <= 0:
                raise ValueError("Valor menor que zero")
            if valor > self._saldo:
                raise ValueError("Valor maior que o saldo")
            self._saldo -= valor
        except:
            raise ValueError("Valor inválido")
        