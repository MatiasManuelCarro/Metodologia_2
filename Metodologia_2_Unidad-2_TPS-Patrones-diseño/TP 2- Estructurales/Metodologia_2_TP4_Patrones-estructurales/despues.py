# ==========================================
# INTERFAZ DEL SERVICIO VIEJO
# ==========================================

class OldGeoServiceInterface:
    def get_location(self, ip: str):
        # tiene que devolver lat, lng, city, country
        raise NotImplementedError("Debe implementarse en la subclase")


# ==========================================
# NUEVA API (Proveedor Moderno)
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
        # Simulación de proveedor moderno
        return Ubicacion(-34.6037, -58.3816, "Buenos Aires", "Argentina")


# ==========================================
# ADAPTER
# ==========================================

class GeoServiceAdapter(OldGeoServiceInterface):

    def __init__(self, provider: NewGeoProvider):
        self.provider = provider

    def get_location(self, ip: str) -> dict:
        ubicacion = self.provider.locate(ip)

        # Traducción al formato viejo 
        return {
            "lat": ubicacion.coordinates.latitude,
            "lng": ubicacion.coordinates.longitude,
            "city": ubicacion.address.locality,
            "country": ubicacion.address.nation
        }

# ==========================================
# FACTORY PARA EL CÓDIGO ANTIGUO (Legacy)
# ==========================================

def OldGeoService():
    #El código viejo sigue llamando al OldGeoService() sin enterarse del cambio.
    return GeoServiceAdapter(NewGeoProvider())


# ==========================================
# CLIENTE ANTES Y DESPUÉS
# ==========================================

#Se puede ver como los archivos viejos pueden seguir funcionando sin enterarse de los cambios
#Tambien los archivos nuevos pueden directamente con el nuevo servicio o el adapter


#Test con el codigo viejo (funciona usando el adapter)
# Los archivos viejos no necesitan ningun tipo de modificacion
def test_antes():
    geo = OldGeoService() #Siguen llamando a OldGeoService()
    data = geo.get_location("200.45.123.10")
    print("[ANTES] Ciudad:", data["city"], "| Latitud:", data["lat"])

#Test con el adapter (se puede utilizar el adapter directamente - solo como demostracion)
def test_adapter():
    geo = GeoServiceAdapter(NewGeoProvider())
    data = geo.get_location("200.45.123.10")
    print("[ADAPTER - DESPUES] Ciudad:", data["city"], "| Latitud:", data["lat"])

"""
Test llamando al nuevo provider directamente (un archivo nuevo puede llamar a la api nueva, sin necesidad de usar 
adapter)
"""
def test_nuevo_servicio():
    geo = NewGeoProvider()
    ubicacion = geo.locate("200.45.123.10")
    print("[NEWGEOPROVIDER] Ciudad", ubicacion.address.locality, "| Latitud: ", ubicacion.coordinates.latitude)



if __name__ == "__main__":
    test_antes()
    test_adapter()
    test_nuevo_servicio()

# ¿qué tendría que cambiar si llega un tercer proveedor mañana?
"""
Si mañana llega un tercer proveedor, lo único que debe modificarse es el Adapter. El sistema legacy sigue llamando a 
`get_location(ip)` y continúa recibiendo un `OldGeoLocation`, por lo que no requiere ningún cambio. El nuevo proveedor
puede tener otra estructura, otros nombres de métodos o incluso otro modelo de datos, pero el Adapter es la única pieza 
encargada de traducir esa nueva API al formato viejo. Mientras la firma `get_location(ip)` se mantenga idéntica y 
el Adapter realice la conversión correcta, el resto del sistema permanece intacto. Esto confirma que el patrón Adapter 
está bien aplicado.
"""

# Justificación del uso de Adapter
"""
Se utiliza el patrón Adapter porque permite integrar un proveedor nuevo sin modificar el código legacy, manteniendo la 
firma original get_location(ip) y el formato de salida esperado. Una refactorización masiva rompería compatibilidad y 
obligaría a actualizar todos los módulos antiguos. Una fachada no resuelve el problema, porque solo simplifica una API,
pero no traduce estructuras incompatibles. El Adapter actúa como una capa de traducción entre dos modelos distintos, 
aislando el cambio y garantizando que el sistema viejo continúe funcionando sin alteraciones.
"""