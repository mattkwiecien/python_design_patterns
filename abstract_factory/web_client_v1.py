from __future__ import annotations
from abc import ABC, abstractmethod
from .api.api_v1 import ApiV1
from .web_client import WebClient


class WebClientV1(WebClient):

    def GetCompanyList(self):
        return ApiV1.get_company_list()
