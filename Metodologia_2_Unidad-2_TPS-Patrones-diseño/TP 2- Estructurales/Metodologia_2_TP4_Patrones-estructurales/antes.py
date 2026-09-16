# ANTES
# LIBRERÍA VIEJA 
class OldGeoService:
    def get_location(self, ip: str) -> dict:
        # Simulacion de algo que devolveria el OldGeoService
        return {
            "lat": -34.6037,
            "lng": -58.3816,
            "city": "Buenos Aires",
            "country": "Argentina"
        }

# Como se llama al OldGeoService en los archivos viejos
# El mismo test esta en el achivo despues con el adapter
def test_antes():
    geo = OldGeoService()
    data = geo.get_location("200.45.123.10")
    print("[ANTES]  Ciudad:", data["city"], "| Latitud:", data["lat"])

if __name__ == "__main__":
    test_antes()