
# Interfaz del Observador
class StockObserver:
    def onLowStock(self, product_id, quantity):
        raise NotImplementedError("Debe implementarse en subclases")

# Excepcion propia para el sistema 
class DomainError(Exception):
    """Error de dominio para fallas en observers."""

#Observadores (implementan la interfaz)
class EmailAlertObserver(StockObserver):
    def onLowStock(self, product_id, quantity):
        print(f"[EMAIL] Stock bajo: {product_id} (stock: {quantity})")


class AnalyticsObserver(StockObserver):
    def onLowStock(self, product_id, quantity):
        print(f"[ANALYTICS] Evento registrado para {product_id}, stock bajo con {quantity} unidades.")


class ReplenishObserver(StockObserver):
    def onLowStock(self, product_id, quantity):
        print(f"[REPLENISH] Orden creada para {product_id}: 100 unidades, stock actual: {quantity}")

# Observador nuevo para extensibilidad
class PushNotificationObserver(StockObserver):
    def onLowStock(self, product_id, quantity):
        print(f"[PUSH] Notificación enviada para {product_id} (stock: {quantity})")


# InventoryManager (Publisher)
class InventoryManager:
    def __init__(self):
        self.observers = []   # lista vacía, sin nombres concretos
        self.stock = {}

    def subscribe(self, observer: StockObserver):
        self.observers.append(observer)

    def unsubscribe(self, observer: StockObserver):
        self.observers.remove(observer)

    def notify(self, product_id, quantity):
        for observer in self.observers:
            try:
                observer.onLowStock(product_id, quantity)
            except DomainError as e:
                print(f"[ERROR] Observer falló: {e}")

    def update_stock(self, product_id, quantity):
        self.stock[product_id] = quantity
        if quantity < 10:
            self.notify(product_id, quantity)

    def sell_product(self, product_id, sold):
        self.stock[product_id] -= sold
        if self.stock[product_id] < 10:
            self.notify(product_id, self.stock[product_id])


# CODIGO DE PRUEBA: Observer roto
class ObserverRoto(StockObserver):
    def onLowStock(self, product_id, quantity):
        raise DomainError("error de red simulado")


# TESTS DEL SISTEMA 

# Test: todos los observers
def test_observers():
    print("\n--- TEST: observers básicos ---")
    manager = InventoryManager()

    manager.subscribe(EmailAlertObserver())
    manager.subscribe(AnalyticsObserver())
    manager.subscribe(ReplenishObserver())

    manager.update_stock("PROD-A", 3)

# Test del observer roto 
def test_observer_roto():
    print("\n--- TEST: observer roto ---")
    manager = InventoryManager()

    manager.subscribe(EmailAlertObserver())
    manager.subscribe(AnalyticsObserver())
    manager.subscribe(ObserverRoto())      # aca falla el observer
    manager.subscribe(ReplenishObserver())   # este debe seguir funcionando

    manager.update_stock("PROD-B", 5)


# Test de extensibilidad: observer nuevo
def test_extensibilidad():
    print("\n--- TEST: extensibilidad ---")
    manager = InventoryManager()

    manager.subscribe(PushNotificationObserver())  # nuevo observer
    manager.update_stock("PROD-C", 2)


# no se dispara nada si el stock no es bajo
def test_no_alertas():
    print("\n--- TEST: stock normal, sin alertas ---")
    manager = InventoryManager()

    manager.subscribe(EmailAlertObserver())
    manager.update_stock("PROD-D", 50)

# sell_product también dispara notificaciones
def test_sell_product():
    print("\n--- TEST: sell_product dispara notificaciones ---")
    manager = InventoryManager()

    manager.subscribe(EmailAlertObserver())
    manager.subscribe(ReplenishObserver())

    manager.stock["PROD-E"] = 12
    manager.sell_product("PROD-E", 5)  # queda en 7 - aviso de stock bajo

# Ejecutar todos los tests

if __name__ == "__main__":
    test_observers()
    test_observer_roto()
    test_extensibilidad()
    test_no_alertas()

#Justificacion
"""
El patrón Observer resolvió el acoplamiento rígido del InventoryManager, que antes dependía directamente de tres servicios concretos. Esto hacía que cualquier cambio, falla o agregado de un nuevo servicio obligará a modificar el  código del manager. También eliminó la duplicación de lógica en update_stock y sell_product. Con Observer, el manager solo conoce una interfaz, no clases concretas, y las notificaciones se vuelven extensibles sin tocar el código central. Además, cada observer maneja sus fallas sin detener a los demás, evitando que un error individual bloquee todo el flujo de notificaciones. 
"""