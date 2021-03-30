import sys
from os import path
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def main():
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)
    else:
        _, file_path, report_type = sys.argv
        importer = {
            ".csv": CsvImporter,
            ".xml": XmlImporter,
            ".json": JsonImporter,
        }
        _, ext = path.splitext(file_path)

        report = InventoryRefactor(importer[ext])
        report = report.import_data(file_path, report_type)
        print(report, end="")
