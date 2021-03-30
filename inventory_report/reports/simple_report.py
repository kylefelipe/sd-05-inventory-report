from operator import itemgetter
from datetime import date


class SimpleReport:
    """
    Classe que gera o relatório simples.
    """

    @classmethod
    def find_nearest_date(cls, products_list):
        now = date.today().strftime("%Y-%m-%d")
        items_list = [
            product
            for product in products_list
            if product["data_de_validade"] >= now
        ]
        near = min(items_list, key=itemgetter("data_de_validade"))
        return near

    @classmethod
    def count_stock(cls, products_list):
        companies = [company["nome_da_empresa"] for company in products_list]
        comp_set = set(companies)
        stock = []
        for company in comp_set:
            quantity = companies.count(company)
            stock.append({"nome_da_empresa": company, "quantity": quantity})
        return max(stock, key=itemgetter("quantity"))

    @classmethod
    def find_oldest_date(cls, products_list):
        return min(products_list, key=itemgetter("data_de_fabricacao"))

    @classmethod
    def generate(cls, products_list):
        report = ""
        oldest = cls.find_oldest_date(products_list)["data_de_fabricacao"]
        report += f"Data de fabricação mais antiga: {oldest}\n"
        nearest = cls.find_nearest_date(products_list)
        report += (
            f"Data de validade mais próxima: {nearest['data_de_validade']}\n"
        )
        bigger = cls.count_stock(products_list).get("nome_da_empresa")
        report += (
            f"Empresa com maior quantidade de produtos estocados: {bigger}\n"
        )
        return report
