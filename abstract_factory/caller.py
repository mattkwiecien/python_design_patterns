from abstract_factory.restservice import RestService
from abstract_factory.webclient import WebClient, WebClientV1, WebClientV2
from abstract_factory.factory import DtoFactory, DtoFactoryV1,\
    DtoFactoryV2
from util import JsonConvert


def main(version):
    factory: DtoFactory
    web_client: WebClient

    if version == 1:
        factory = DtoFactoryV1()
        web_client = WebClientV1()
    else:
        factory = DtoFactoryV2()
        web_client = WebClientV2()

    rest = RestService(factory, web_client)
    my_company_list = rest.get_company_list()
    return my_company_list


if __name__ == "__main__":
    version_independent_list = main(1)
    print(version_independent_list)

    # Even though V2 changed the address property, the existing code didn't
    # have to change, only adding a new version 2 implementation.
    version_independent_list = main(2)
    print(version_independent_list)
