from __future__ import annotations
from abc import ABC, abstractmethod


class WebClient(ABC):

    @abstractmethod
    def GetCompanyList(self):
        pass
