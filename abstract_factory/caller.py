from abstract_factory.restservice import RestService
from abstract_factory.webclient import WebClient, WebClientV1, WebClientV2
from abstract_factory.factory import DtoFactory, DtoFactoryV1,\
    DtoFactoryV2


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
    my_company_list = rest.GetCompanyList()
    print(my_company_list)


if __name__ == "__main__":
    main(1)
    main(2)
