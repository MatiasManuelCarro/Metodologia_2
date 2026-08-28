from enum import Enum
from abc import ABC, abstractmethod

# Definimos enums para restringir valores válidos
class CarType(Enum):
    SUV = "SUV"
    CAMIONETA = "Camioneta"
    SEDAN = "Sedán"

class EngineType(Enum):
    V8 = "V8"
    DIESEL = "Diesel"
    MOTOR_2_0 = "Motor 2.0"

# Producto
class Car:
    def __init__(self):
        self.type = None
        self.seats = None
        self.engine = None

    def __str__(self):
        return f"Car(type={self.type}, seats={self.seats}, engine={self.engine})"

# Interfaz Builder
class Builder(ABC):
    @abstractmethod
    def set_type(self, car_type: CarType): pass
    @abstractmethod
    def set_seats(self, seats: int): pass
    @abstractmethod
    def set_engine(self, engine: EngineType): pass
    @abstractmethod
    def build(self) -> Car: pass

# Implementación concreta
class CarBuilder(Builder):
    def __init__(self):
        self.car = Car()

    def set_type(self, car_type: CarType):
        self.car.type = car_type
        return self

    def set_seats(self, seats: int):
        self.car.seats = seats
        return self

    def set_engine(self, engine: EngineType):
        self.car.engine = engine
        return self

    def build(self) -> Car:
        return self.car

# Uso
if __name__ == "__main__":
    suv = CarBuilder().set_type(CarType.SUV).set_seats(5).set_engine(EngineType.V8).build()
    camioneta = CarBuilder().set_type(CarType.CAMIONETA).set_seats(2).set_engine(EngineType.DIESEL).build()
    sedan = CarBuilder().set_type(CarType.SEDAN).set_seats(4).set_engine(EngineType.MOTOR_2_0).build()

    print(suv)
    print(camioneta)
    print(sedan)
