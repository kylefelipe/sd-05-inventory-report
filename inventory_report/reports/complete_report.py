from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def get_companies_stock(cls, products_list):
        companies = [company["nome_da_empresa"] for company in products_list]
        comp_set = {company: companies.count(company) for company in companies}
        stock = []
        for company in comp_set.keys():
            stock.append(
                {"nome_da_empresa": company, "quantity": comp_set[company]}
            )
        return stock

    @classmethod
    def generate(cls, products_list):
        report = super().generate(products_list)
        report += "\n"
        report += "Produtos estocados por empresa: \n"
        for company in cls.get_companies_stock(products_list):
            stk = list(company.values())
            report += f"- {stk[0]}: {stk[1]}\n"
        return report
