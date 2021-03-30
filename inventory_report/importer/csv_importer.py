import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    """
    Importa um CSV
    """

    data = []

    @classmethod
    def import_data(cls, file_path):
        if not file_path.endswith(".csv"):
            raise ValueError("Arquivo inválido")
        else:
            with open(file_path, "r") as file:
                data = csv.DictReader(file, delimiter=",")
                cls.data = list(data)
        return cls.data
