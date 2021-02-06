from abstract_factory.webclient import WebClient
from abstract_factory.factory.dto_factory import DtoFactory


class RestService(object):

    _factory: DtoFactory
    _web_client: WebClient

    def __init__(self, api_dto_factory: DtoFactory, web_client: WebClient):
        self._factory = api_dto_factory
        self._web_client = web_client

    def GetCompanyList(self):
        responseJson = self._web_client.company_list()
        companyDtoList = self._factory.company_list(responseJson)
        return companyDtoList
