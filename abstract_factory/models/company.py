from abstract_factory.factory.company import CompanyDto


class Company(object):
    def __init__(self, company_dto: CompanyDto):
        self.name = company_dto.name
        self.id = company_dto.id
        self.address = company_dto.address
