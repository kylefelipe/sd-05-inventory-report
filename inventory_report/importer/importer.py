from abc import ABC, abstractmethod


class Importer(ABC):
    """
    Super classe para definir a assinatura das sub classes
    """

    @abstractmethod
    def import_data(self, file_path):
        """
        Importa o arquivo passado no parametro file_path
        """
        ...
