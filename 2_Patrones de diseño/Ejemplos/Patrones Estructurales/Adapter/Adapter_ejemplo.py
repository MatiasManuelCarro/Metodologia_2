from abc import ABC, abstractmethod

# 1. La interfaz Objetivo (Target)
class ProcesadorPago(ABC):
    @abstractmethod
    def pagar_en_pesos(self, cantidad: float):
        pass

# 2. La clase Incompatible (Adaptee)
class PasarelaInternacional:
    def pay_in_dollars(self, amount: float):
        print(f"Pagando ${amount:.2f} USD")

# 3. El Adaptador (Adapter)
class AdaptadorPagoInternacional(ProcesadorPago):
    def __init__(self, pasarela: PasarelaInternacional):
        self.pasarela = pasarela
        self.tipo_de_cambio = 1000.0

    def pagar_en_pesos(self, cantidad: float):
        dolares = cantidad / self.tipo_de_cambio
        self.pasarela.pay_in_dollars(dolares)

# 4. Código Cliente (Ejecución)
if __name__ == "__main__":
    # Instanciamos la clase incompatible
    pasarela = PasarelaInternacional()
    
    # Envolvemos la clase incompatible con nuestro adaptador
    procesador = AdaptadorPagoInternacional(pasarela)
    
    # El cliente usa el método que conoce
    procesador.pagar_en_pesos(50000)