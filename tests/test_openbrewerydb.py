import random
import pytest
from jsonschema import validate

from api_client.api_client_openbrewerydb import ApiClientBreweries
from utils import CheckStatusCode

checkStatusCode = CheckStatusCode()
apiClient = ApiClientBreweries()


class TestBreweries:
    @pytest.mark.parametrize('method, param, check',
                             [(apiClient.get_brewery_by_id, '2432525', checkStatusCode.isClientError),
                              (apiClient.get_brewery_by_id, '44', checkStatusCode.isSuccess),
                              (apiClient.get_brewery_by_city, 'Alameda', checkStatusCode.isSuccess),
                              (apiClient.get_brewery_by_name, 'MadTree Brewing', checkStatusCode.isSuccess),
                              (apiClient.get_brewery_by_postal, '45209-1132', checkStatusCode.isSuccess),
                              (apiClient.get_brewery_by_state, 'California', checkStatusCode.isSuccess),
                              (apiClient.get_brewery_by_city, 'Oakland', checkStatusCode.isSuccess),
                              (apiClient.get_brewery_by_tag, 'dog-friendly', checkStatusCode.isSuccess),
                              (apiClient.get_brewery_by_tags, 'dog-friendly, tours', checkStatusCode.isSuccess),
                              (apiClient.get_brewery_by_type, 'brewpub', checkStatusCode.isSuccess),
                              (apiClient.get_brewery_page, '1', checkStatusCode.isSuccess),
                              (apiClient.get_brewery_with_autocomplete, 'dog', checkStatusCode.isSuccess)])
    def test_status_code(self, method, param, check):
        response = method(param)
        check(response)

    def test_brewery_schema(self, brewery_schema):
        response = apiClient.get_brewery_by_id('1134')
        schema = brewery_schema
        validate(instance=response.json(), schema=schema)

    def test_random_brewery_id(self):
        random_id = str(random.randint(1, 15000))
        response = apiClient.get_brewery_by_id(random_id)
        try:
            checkStatusCode.isSuccess(response)
            print("Brewery for you is found!")
        except AssertionError:
            checkStatusCode.isClientError(response)
            print("Sorry, brewery with this id doesn't exist")

    def test_brewery_types(self, brewery_types):
        response = apiClient.get_brewery_by_type(brewery_types)
        actual_brewery_type = response.json()[0]['brewery_type']
        assert actual_brewery_type == brewery_types

    def test_brewery_by_tags(self):
        response = apiClient.get_brewery_by_tags('dog-friendly', 'patio')
        checkStatusCode.isSuccess(response)
