from __future__ import annotations
from abc import ABC, abstractmethod
from abstract_factory.factory.company import CompanyDto, CompanyV1, CompanyV2
from util import JsonConvert


class DtoFactory(ABC):
    @abstractmethod
    def company_list(self, json) -> CompanyDto:
        pass


class DtoFactoryV1(DtoFactory):
    def company_list(self, json) -> CompanyDto:
        companies = JsonConvert.deserialize(json)

        dtos = []
        for c in companies:
            dtos.append(CompanyV1(c))

        return dtos


class DtoFactoryV2(DtoFactory):
    def company_list(self, json) -> CompanyDto:
        companies = JsonConvert.deserialize(json)

        dtos = []
        for c in companies:
            dtos.append(CompanyV2(c))

        return dtos
