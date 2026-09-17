from dataclasses import dataclass
from enum import Enum

class CarType(Enum):
    SUV = "SUV"
    CAMIONETA = "Camioneta"
    SEDAN = "Sedán"

@dataclass
class Car:
    type: CarType
    seats: int
    engine: str

# Uso directo, sin builder
autos = [
    Car(type=CarType.SUV, seats=5, engine="V8"),
    Car(type=CarType.CAMIONETA, seats=2, engine="Diesel"),
    Car(type=CarType.SEDAN, seats=4, engine="Motor 2.0")
]

for auto in autos:
    print(auto)