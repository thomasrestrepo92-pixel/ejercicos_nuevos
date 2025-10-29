# clase cuenta con atributos privados y metodos para manejar saldo
class cuenta:

    #metodo constructor inicializar los atributos
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.__saldo = cantidad # atributo privado

    #metodos para acceder y modificar saldo
    def get_cantidad(self):
        return self.__saldo
    
    #metodos para ingresar y retirar dinero
    def ingresar(self, monto):
        if monto > 0:
            self.__saldo += monto

    def retirar(self, monto):
        if monto > 0 and self.__saldo >= monto:
            self.__saldo -= monto

    def mostrar_info(self):
        return f"titular: {self.titular} * cantidad $ {self.__saldo}"
    

#ejemplo de uso de la clase cuenta
if __name__ == "__main__":
    cuenta = cuenta("juan perez", 1000000)
    print(cuenta.mostrar_info())

    cuenta.ingresar(500000)
    print("saldo actualizado despues de su deposito:")
    print(cuenta.mostrar_info())

    cuenta.retirar(200000)
    print("saldo de cuenta actualizado despues de su retiro")
    print(cuenta.mostrar_info())    