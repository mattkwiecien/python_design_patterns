import json


class ApiV2(object):

    @staticmethod
    def get_company_list():
        companies = [
            ApiCompanyV2(
                "Test 1",
                "1",
                "1234 Fake Ave",
                "Chicago",
                "IL",
                "60606"
            ),
            ApiCompanyV2(
                "Test 2",
                "2",
                "1234 Fake Ave",
                "Chicago",
                "IL",
                "60606"
            ),
            ApiCompanyV2(
                "Test 3",
                "3",
                "1234 Fake Ave",
                "Chicago",
                "IL",
                "60606"
            )
        ]
        return json.dumps(companies)


class ApiCompanyV2(object):

    def __init__(self, name, id, st_address, city, st, zip):
        self.name = name
        self.id = id
        self.st_address = st_address
        self.city = city
        self.st = st
        self.zip = zip
