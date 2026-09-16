class EmailAlertService:
    def send_low_stock_alert(self, product_id, quantity):
        print(f"[EMAIL] Alerta: stock bajo para {product_id} (qty={quantity})")


class AnalyticsDashboard:
    def record_low_stock_event(self, product_id):
        print(f"[ANALYTICS] Evento registrado para {product_id}")


class AutoReplenishment:
    def trigger_order(self, product_id, amount):
        print(f"[REPLENISH] Orden creada para {product_id}: {amount} unidades")


class InventoryManager:
    def __init__(self):
        self.emailService = EmailAlertService()
        self.analytics = AnalyticsDashboard()
        self.replenishment = AutoReplenishment()
        self.stock = {}

    def update_stock(self, product_id, quantity):
        self.stock[product_id] = quantity

        if quantity < 10:
            self.emailService.send_low_stock_alert(product_id, quantity)
            self.analytics.record_low_stock_event(product_id)
            self.replenishment.trigger_order(product_id, 100)

    def sell_product(self, product_id, sold):
        self.stock[product_id] -= sold

        if self.stock[product_id] < 10:
            self.emailService.send_low_stock_alert(product_id, self.stock[product_id])
            self.analytics.record_low_stock_event(product_id)
            self.replenishment.trigger_order(product_id, 100)


# TESTS DEL CÓDIGO "ANTES"

def test_update_stock_low():
    print("\n--- TEST: update_stock con stock bajo ---")
    manager = InventoryManager()
    manager.update_stock("PROD-001", 5)


def test_sell_product_low():
    print("\n--- TEST: sell_product con stock bajo ---")
    manager = InventoryManager()
    manager.stock["PROD-002"] = 12
    manager.sell_product("PROD-002", 5)


def test_no_alerts():
    print("\n--- TEST: stock normal, no hay alertas ---")
    manager = InventoryManager()
    manager.update_stock("PROD-003", 50)


class PushNotificationService:
    def send_push(self, product_id, qty):
        print(f"[PUSH] Notificación: stock bajo para {product_id} (qty={qty})")


if __name__ == "__main__":
    test_update_stock_low()
    test_sell_product_low()
    test_no_alerts()
