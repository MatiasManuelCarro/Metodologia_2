class ReportService:
    def generate(self, data, format_type):
        # decisión de construcción mezclada con lógica de uso
        if format_type == "pdf":
            report = PDFReport()
        elif format_type == "excel":
            report = ExcelReport()
        elif format_type == "csv":
            report = CSVReport()
        else:
            raise Exception("Formato no soportado")

        # lógica de uso — igual para todos los tipos
        report.set_data(data)
        report.add_header("Reporte Mensual")
        report.add_footer("Generado el " + hoy())
        report.render()
        return report.get_output()
