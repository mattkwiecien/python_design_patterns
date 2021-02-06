from abc import ABC, abstractmethod
from abstract_factory.api import ApiCompanyV1, ApiCompanyV2


class CompanyDto(ABC):
    """
    Represents a version independent object.\r\n
    The rest of the code can directly depend on this object, without
    worrying about breaking changes from the external API.
    """

    def __init__(self):
        self.name = ""
        self.id = ""
        self.address = ""

    def __repr__(self):
        return "Name: " + self.name + ", ID: " + self.id \
            + ", Address: " + self.address


class CompanyV1(CompanyDto):
    def __init__(self, dto: ApiCompanyV1):
        self.name = dto.name
        self.id = dto.id
        self.address = dto.address


class CompanyV2(CompanyDto):
    def __init__(self, dto: ApiCompanyV2):
        self.name = dto.name
        self.id = dto.id
        self.st_address = dto.st_address
        self.city = dto.city
        self.st = dto.st
        self.zip = dto.zip

    @property
    def address(self):
        return self.st_address + ", " + self.city + ", " + self.st + ", " + \
            self.zip
