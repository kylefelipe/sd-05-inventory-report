from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.data = []
        self.importer = importer

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, file_path, report_type):
        """
        Importa o arquivo informado em file_path e retorna o relatório
        PARAMS:
        - file_path: STRING - caminho do arquivo
        - report_type: STRING - tipo do relatório (simples | completo)
        """
        self.data.extend(self.importer.import_data(file_path))
        if report_type == "simples":
            return SimpleReport.generate(self.data)
        if report_type == "completo":
            return CompleteReport.generate(self.data)
