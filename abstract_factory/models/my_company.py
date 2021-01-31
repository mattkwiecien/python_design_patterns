from ..factory.company import CompanyDto


class MyCompany(object):
    def __init__(self, company_dto: CompanyDto):
        self.name = company_dto.name
        self.id = company_dto.id
        self.address = company_dto.address
