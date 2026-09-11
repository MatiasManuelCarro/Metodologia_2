
# ==========================================
# NUEVA API
# ==========================================
class Coordinates:
    def __init__(self, lat: float, lng: float):
        self.latitude = lat
        self.longitude = lng

class Address:
    def __init__(self, locality: str, nation: str):
        self.locality = locality
        self.nation = nation

class Ubicacion:
    def __init__(self, lat: float, lng: float, locality: str, nation: str):
        self.coordinates = Coordinates(lat, lng)
        self.address = Address(locality, nation)

class NewGeoProvider:
    def locate(self, ip: str) -> Ubicacion:
        return Ubicacion(-34.6037, -58.3816, "Buenos Aires", "Argentina")
# ==========================================
# ADAPTER
# ==========================================
class GeoServiceAdapter:  
    
    def __init__(self):
        self.provider = NewGeoProvider()

    def get_location(self, ip: str) -> dict:
        # Misma funcion que el sistema espera
        # Llama al nuevo proveedor
        geo_locacion = self.provider.locate(ip) 
        
        # Traduce la respuesta al formato viejo
        return {
            "lat": geo_locacion.coordinates.latitude,
            "lng": geo_locacion.coordinates.longitude,
            "city": geo_locacion.address.locality,
            "country": geo_locacion.address.nation
        }

# Se instancia que archivo o programa que llame a OldGeoService en realidad reciba GeoServiceADapater
OldGeoService = GeoServiceAdapter


# ==========================================
# 4. CÓDIGO CLIENTE Antes y Despues
# ==========================================

# Los archivos antiguos pueden llamar al OldGeoService, los nuevos pueden llamar al adpater 
# (o continuar con oldgeoservice sin problemas)

def test():
    geo = OldGeoService()
    data = geo.get_location("200.45.123.10")
    print(f"[ANTES]   Ciudad: {data['city']}, Lat: {data['lat']}")

def test_adapter():
    geo = GeoServiceAdapter()    
    data = geo.get_location("200.45.123.10")
    print(f"[DESPUÉS] Ciudad: {data['city']}, Lat: {data['lat']}")


if __name__ == "__main__":
    test()
    test_adapter()