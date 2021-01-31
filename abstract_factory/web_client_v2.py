from __future__ import annotations
from abc import ABC, abstractmethod
from .api.api_v2 import ApiV2
from .web_client import WebClient


class WebClientV2(WebClient):

    def GetCompanyList(self):
        return ApiV2.get_company_list()
