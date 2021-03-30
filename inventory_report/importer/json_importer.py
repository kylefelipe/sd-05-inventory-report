import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    """
    Importa um JSON
    """

    data = []

    @classmethod
    def import_data(cls, file_path):
        if not file_path.endswith(".json"):
            raise ValueError("Arquivo inválido")
        else:
            with open(file_path, "r") as file:
                cls.data = json.loads(file.read())
        return cls.data


if __name__ == "__main__":
    f_path = "inventory_report/data/inventory"
    f_ext = ".json"
    print(JsonImporter.import_data(f_path + f_ext))
