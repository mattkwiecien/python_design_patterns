from __future__ import annotations
from abc import ABC, abstractmethod
from abstract_factory.api import ApiV1
from abstract_factory.api import ApiV2


class WebClient(ABC):

    @abstractmethod
    def company_list(self):
        pass


class WebClientV1(WebClient):

    def company_list(self):
        return ApiV1.list_companies()


class WebClientV2(WebClient):

    def company_list(self):
        return ApiV2.list_companies()
