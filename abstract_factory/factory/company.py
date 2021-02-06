from abc import ABC, abstractmethod


class CompanyDto(ABC):
    name = ""
    id = ""
    address = ""


class CompanyV1(CompanyDto):
    pass


class CompanyV2(CompanyDto):
    st_address = ""
    city = ""
    st = ""
    zip = ""

    @property
    def address(self):
        return self.st_address + ", " + self.city + ", " + self.st + ", " + \
            self.zip

    pass
