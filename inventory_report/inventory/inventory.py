import csv
import json
import xmltodict
from os import path
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    data = []
    file_path = None

    @classmethod
    def import_csv(cls):
        with open(cls.file_path, "r") as file:
            reader = csv.reader(file)
            header, *content = reader
        cls.data = [dict(zip(header, row)) for row in content]
        return True

    @classmethod
    def import_json(cls):
        with open(cls.file_path, "r") as file:
            cls.data = json.loads(file.read())
        return True

    @classmethod
    def import_xml(cls):
        with open(cls.file_path, "r") as file:
            parsed_data = xmltodict.parse(file.read())
            cls.data = [
                dict(product) for product in parsed_data["dataset"]["record"]
            ]
        return True

    @classmethod
    def import_data(cls, file_path, report_type):
        """
        Importa os dados para ser utilizado no relatório:
        PARAMS:
        - file_path: STRING, caminho do arquivo.
        - report_type: STRING tipo de relatório ("simples", "completo").
        """
        formats = {
            ".csv": cls.import_csv,
            ".xml": cls.import_xml,
            ".json": cls.import_json,
        }
        cls.file_path = file_path
        file_format = path.splitext(file_path)[1]
        formats.get(file_format)()
        if report_type == "simples":
            return SimpleReport.generate(cls.data)
        elif report_type == "completo":
            return CompleteReport.generate(cls.data)
