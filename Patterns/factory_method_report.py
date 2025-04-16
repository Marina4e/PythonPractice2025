from abc import ABC, abstractmethod


# Абстрактний продукт (інтерфейс для створення звітів)
class Report(ABC):
    @abstractmethod
    def generate(self, data: str) -> None:
        pass


# Конкретні продукти (реалізації для різних форматів звітів)
class PDFReport(Report):
    def generate(self, data: str) -> None:
        print(f"Generating PDF report with data: {data}")


class ExcelReport(Report):
    def generate(self, data: str) -> None:
        print(f"Generating Excel report with data: {data}")


class HTMLReport(Report):
    def generate(self, data: str) -> None:
        print(f"Generating HTML report with data: {data}")


# Абстрактна фабрика
class ReportFactory(ABC):
    @abstractmethod
    def create_report(self) -> Report:
        pass


# Конкретні фабрики
class PDFReportFactory(ReportFactory):
    def create_report(self) -> Report:
        return PDFReport()


class ExcelReportFactory(ReportFactory):
    def create_report(self) -> Report:
        return ExcelReport()


class HTMLReportFactory(ReportFactory):
    def create_report(self) -> Report:
        return HTMLReport()


# Приклад використання
def client_code(report_factory: ReportFactory, data: str):
    report = report_factory.create_report()
    report.generate(data)


# Використання різних фабрик для створення звітів
client_code(PDFReportFactory(), "Sales Data")  # Виведе: Generating PDF report with data: Sales Data
client_code(ExcelReportFactory(), "Sales Data")  # Виведе: Generating Excel report with data: Sales Data
client_code(HTMLReportFactory(), "Sales Data")  # Виведе: Generating HTML report with data: Sales Data
