import json


class ApiV1(object):

    @staticmethod
    def list_companies():
        companies = [
            ApiCompanyV1(
                "Test 1",
                "1",
                "1234 Fake Ave, Chicago, IL, 60606"
            ),
            ApiCompanyV1(
                "Test 2",
                "2",
                "1234 Fake Ave, Chicago, IL, 60606"
            ),
            ApiCompanyV1(
                "Test 3",
                "3",
                "1234 Fake Ave, Chicago, IL, 60606"
            )
        ]
        return json.dumps(companies)


class ApiCompanyV1(object):

    def __init__(self, name, id, address):
        self.name = name
        self.id = id
        self.address = address
