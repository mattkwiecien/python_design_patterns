from __future__ import annotations
from abc import ABC, abstractmethod
from ..factory.company import CompanyDto, CompanyV1
from ..factory.api_dto_factory import ApiDtoFactory

class ApiDtoFactoryV1(ApiDtoFactory):
    def create_company(self, json) -> CompanyDto:
        return CompanyV1()
