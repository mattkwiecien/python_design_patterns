from __future__ import annotations
from abc import ABC, abstractmethod
from abstract_factory.factory.company import CompanyDto, CompanyV1, CompanyV2


class DtoFactory(ABC):
    @abstractmethod
    def company_list(self, json) -> CompanyDto:
        pass


class DtoFactoryV1(DtoFactory):
    def company_list(self, json) -> CompanyDto:
        return CompanyV1()


class DtoFactoryV2(DtoFactory):
    def company_list(self, json) -> CompanyDto:
        return CompanyV2()
