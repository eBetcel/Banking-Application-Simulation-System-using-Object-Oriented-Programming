from ContaCorrente import ContaCorrente
from Cliente import Cliente

def main():
    cliente = Cliente()
    conta = ContaCorrente(Cliente("Fulano", "123456789-00"), "1234-5", "1234", 1000)

if __name__ == "__main__":
    main()
