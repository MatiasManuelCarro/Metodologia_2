from abc import ABC, abstractmethod
from datetime import date

# 1. La interfaz que todos los reportes cumplen
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
class PDFReport(Report):
    def __init__(self):
        self.content = []

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
        self.rows = []

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
        self.lines = []

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
        self.html = []

    def set_data(self, data):
        self.html.append(f"HTML Data: {data}")

    def add_header(self, text):
        self.html.insert(0, f"HTML Header: {text}")

    def add_footer(self, text):
        self.html.append(f"HTML footer: {text}")

    def render(self):
        self.html.append("HTML Rendered")

    def get_output(self) -> str:
        return "\n".join(self.html)


# 3. La fábrica concentra la decisión de construcción
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
class ReportService:
    def generate(self, data, format_type):
        report = ReportFactory.create(format_type)  # no sabe qué tipo es
        report.set_data(data)
        report.add_header("Reporte Mensual")
        report.add_footer("Generado el " + str(date.today()))
        report.render()
        return report.get_output()


# Ejemplo de uso
servicio = ReportService()
print(servicio.generate("Datos en html", "html"))
print("=======================")
print(servicio.generate("Datos de csv", "csv"))




# Se uso Factory Method porque alcanza con una fábrica que decida
# qué tipo de reporte crear. El servicio no necesita saber si es PDF,
# Excel o CSV, solo lo usa. Esto evita acoplar el código y permite
# agregar nuevos formatos sin tocar la lógica del servicio.
