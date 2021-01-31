from __future__ import annotations
from abc import ABC, abstractmethod
from ..factory.Company import CompanyDto, CompanyV1, CompanyV2

class ApiDtoFactory(ABC):
    @abstractmethod
    def create_company(self, json) -> CompanyDto:
        pass
