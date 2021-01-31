from .web_client import WebClient
from .factory.api_dto_factory import ApiDtoFactory

class RestService(object):

    def __init__(self, api_dto_factory: ApiDtoFactory, web_client: WebClient):
        self._api_dto_factory = api_dto_factory
        self._web_client = web_client


    def get_company_list(self):
        responseJson = self._web_client.get_company_list()
        companyDtoList = self._api_dto_factory.create_company_dtos(responseJson)
        return companyDtoList