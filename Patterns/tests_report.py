from contextlib import redirect_stdout
from io import StringIO

import pytest

from examples_factory_method.factory_method_report import PDFReportFactory, ExcelReportFactory, HTMLReportFactory, \
    client_code


@pytest.fixture
def capture_stdout():
    """Фікстура для перехоплення виводу в stdout."""
    output = StringIO()
    with redirect_stdout(output):
        yield output
    return output.getvalue()


# Тести для PDFReportFactory
def test_pdf_report_factory(capture_stdout):
    """Тестуємо генерацію PDF звіту"""
    with redirect_stdout(capture_stdout):
        client_code(PDFReportFactory(), "Test Data")
    output = capture_stdout.getvalue().strip()
    assert output == "Generating PDF report with data: Test Data"


# Тести для ExcelReportFactory
def test_excel_report_factory(capture_stdout):
    """Тестуємо генерацію Excel звіту"""
    with redirect_stdout(capture_stdout):
        client_code(ExcelReportFactory(), "Test Data")
    output = capture_stdout.getvalue().strip()
    assert output == "Generating Excel report with data: Test Data"


# Тести для HTMLReportFactory
def test_html_report_factory(capture_stdout):
    """Тестуємо генерацію HTML звіту"""
    with redirect_stdout(capture_stdout):
        client_code(HTMLReportFactory(), "Test Data")
    output = capture_stdout.getvalue().strip()
    assert output == "Generating HTML report with data: Test Data"
