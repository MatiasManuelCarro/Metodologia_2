from abc import ABC, abstractmethod
from datetime import date

# 1. La interfaz que todos los reportes cumplen
# Usamos una clase abstracta (ABC) para definir la "contrato" que todas las clases concretas deben respetar.
# Esto asegura que cada reporte tenga los mismos métodos (set_data, add_header, etc.).
class Report(ABC):
    
    @abstractmethod
    def set_data(self, data):
        pass

    @abstractmethod
    def add_header(self, text):
        pass

    @abstractmethod
    def add_footer(self, text):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def get_output(self) -> str:
        pass


# 2. Las clases concretas
# Cada clase implementa la interfaz Report, pero con su propia lógica interna.
# Esto permite que ReportService use cualquier tipo de reporte sin saber cómo funciona por dentro.

class PDFReport(Report):
    def __init__(self):
        self.content = []  # estructura interna para guardar datos

    def set_data(self, data):
        self.content.append(f"PDF Data: {data}")

    def add_header(self, text):
        self.content.insert(0, f"PDF Header: {text}")

    def add_footer(self, text):
        self.content.append(f"PDF Footer: {text}")

    def render(self):
        self.content.append("PDF Rendered")

    def get_output(self) -> str:
        return "\n".join(self.content)


class ExcelReport(Report):
    def __init__(self):
        self.rows = []  # estructura interna distinta a PDF

    def set_data(self, data):
        self.rows.append(f"Excel Data: {data}")

    def add_header(self, text):
        self.rows.insert(0, f"Excel Header: {text}")

    def add_footer(self, text):
        self.rows.append(f"Excel Footer: {text}")

    def render(self):
        self.rows.append("Excel Rendered")

    def get_output(self) -> str:
        return "\n".join(self.rows)


class CSVReport(Report):
    def __init__(self):
        self.lines = []  # otra estructura interna

    def set_data(self, data):
        self.lines.append(f"CSV Data: {data}")

    def add_header(self, text):
        self.lines.insert(0, f"CSV Header: {text}")

    def add_footer(self, text):
        self.lines.append(f"CSV Footer: {text}")

    def render(self):
        self.lines.append("CSV Rendered")

    def get_output(self) -> str:
        return "\n".join(self.lines)


class HTMLReport(Report):
    def __init__(self):
        self.html = []  # estructura pensada para HTML

    def set_data(self, data):
        self.html.append(f"<p>{data}</p>")

    def add_header(self, text):
        self.html.insert(0, f"<h1>{text}</h1>")

    def add_footer(self, text):
        self.html.append(f"<footer>{text}</footer>")

    def render(self):
        self.html.append("<!-- HTML Rendered -->")

    def get_output(self) -> str:
        return "\n".join(self.html)


# 3. La fábrica concentra la decisión de construcción
# Aquí está el Factory Method (variante estática).
# La lógica de "qué clase instanciar" está aislada en un solo lugar.
# ReportService no necesita conocer las clases concretas.
class ReportFactory:
    @staticmethod
    def create(format_type: str) -> Report:
        if format_type == "pdf":
            return PDFReport()
        elif format_type == "excel":
            return ExcelReport()
        elif format_type == "csv":
            return CSVReport()
        elif format_type == "html":
            return HTMLReport()
        else:
            raise ValueError("Formato no soportado")


# 4. El servicio ahora es agnóstico al formato
# ReportService solo sabe que existe una fábrica que le da un "Report".
# No importa si es PDF, Excel, CSV o HTML: la lógica de uso es la misma.
class ReportService:
    def generate(self, data, format_type):
        report = ReportFactory.create(format_type)  # delega la construcción a la fábrica
        report.set_data(data)
        report.add_header("Reporte Mensual")
        report.add_footer("Generado el " + str(date.today()))
        report.render()
        return report.get_output()


# Ejemplo de uso
# El cliente pide un reporte HTML. ReportService no sabe cómo se construye,
# solo sabe que puede usarlo porque cumple la interfaz Report.
servicio = ReportService()
print(servicio.generate("Datos de prueba", "html"))


# ---------------------------------------------------------
# ¿Por qué Factory Method y no Abstract Factory?
# Abstract Factory se usa para crear familias de objetos relacionados
# (ej. botón + input + checkbox con mismo tema visual).
# En este caso solo hay un tipo de objeto (Report) en distintas variantes.
# Factory Method (variante estática) es suficiente porque encapsula
# la decisión de construcción de un único objeto.
# ---------------------------------------------------------
