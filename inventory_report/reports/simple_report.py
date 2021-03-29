from operator import itemgetter
from datetime import date

example = [
    {
        "id": 1,
        "nome_do_produto": "CALENDULA OFFICINALIS FLOWERING TOP",
        "nome_da_empresa": "Forces of Nature",
        "data_de_fabricacao": "2020-07-04",
        "data_de_validade": "2023-02-09",
        "numero_de_serie": "FR48 2002 7680 97V4 W6FO LEBT 081",
        "instrucoes_de_armazenamento": "in blandit ultrices enim",
    },
    {
        "id": 2,
        "nome_do_produto": "sodium ferric gluconate complex",
        "nome_da_empresa": "sanofi-aventis U.S. LLC",
        "data_de_fabricacao": "2020-05-31",
        "data_de_validade": "2023-01-17",
        "numero_de_serie": "SE95 2662 8860 5529 8299 2861",
        "instrucoes_de_armazenamento": "duis bibendum morbi",
    },
    {
        "id": 3,
        "nome_do_produto": "Dexamethasone Sodium Phosphate",
        "nome_da_empresa": "sanofi-aventis U.S. LLC",
        "data_de_fabricacao": "2019-09-13",
        "data_de_validade": "2023-02-13",
        "numero_de_serie": "BA52 2034 8595 7904 7131",
        "instrucoes_de_armazenamento": "morbi quis tortor id",
    },
    {
        "id": 4,
        "nome_do_produto": "Uricum acidum, Benzoicum acidum",
        "nome_da_empresa": "Newton Laboratories, Inc.",
        "data_de_fabricacao": "2019-11-08",
        "data_de_validade": "2019-11-25",
        "numero_de_serie": "FR38 9203 3060 400T QQ8B HHS0 Q46",
        "instrucoes_de_armazenamento": "velit eu est congue elementum",
    },
]


class SimpleReport:
    @classmethod
    def find_nearest_date(self, products_list):
        now = date.today().strftime("%Y-%m-%d")
        items_list = [
            product
            for product in products_list
            if product["data_de_validade"] >= now
        ]
        near = min(items_list, key=itemgetter("data_de_validade"))
        return near

    @classmethod
    def count_stock(self, products_list):
        companies = [company["nome_da_empresa"] for company in products_list]
        comp_set = set(companies)
        stock = []
        for company in comp_set:
            quantity = companies.count(company)
            stock.append({"nome_da_empresa": company, "quantity": quantity})
        return max(stock, key=itemgetter("quantity"))

    @classmethod
    def find_oldest_date(self, products_list):
        return min(products_list, key=itemgetter("data_de_fabricacao"))

    @classmethod
    def generate(self, products_list):
        report = ""
        oldest = self.find_oldest_date(products_list)["data_de_fabricacao"]
        report += f"Data de fabricação mais antiga: {oldest}\n"
        nearest = self.find_nearest_date(products_list)
        report += (
            f"Data de validade mais próxima: {nearest['data_de_validade']}\n"
        )
        bigger = self.count_stock(products_list).get("nome_da_empresa")
        report += (
            f"Empresa com maior quantidade de produtos estocados: {bigger}\n"
        )
        return report


if __name__ == "__main__":
    print(SimpleReport.generate(example))
