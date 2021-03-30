import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    """
    Importa um Xml
    """

    data = []

    @classmethod
    def import_data(cls, file_path):
        if not file_path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        else:
            with open(file_path, "r") as file:
                parsed_data = xmltodict.parse(file.read())
                cls.data = [
                    dict(product)
                    for product in parsed_data["dataset"]["record"]
                ]
        return cls.data
