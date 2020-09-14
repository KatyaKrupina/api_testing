import random
import pytest
from jsonschema import validate

from api_client.api_client_openbrewerydb import ApiClientBreweries
from utils import CheckStatusCode

checkStatusCode = CheckStatusCode()
apiClient = ApiClientBreweries()


class TestBreweries:
    @pytest.mark.parametrize('method, param, check',
                             [(apiClient.get_brewery_by_id, '2432525', checkStatusCode.is_not_found),
                              (apiClient.get_brewery_by_id, '44', checkStatusCode.is_success),
                              (apiClient.get_brewery_by_city, 'Alameda', checkStatusCode.is_success),
                              (apiClient.get_brewery_by_name, 'MadTree Brewing', checkStatusCode.is_success),
                              (apiClient.get_brewery_by_postal, '45209-1132', checkStatusCode.is_success),
                              (apiClient.get_brewery_by_state, 'California', checkStatusCode.is_success),
                              (apiClient.get_brewery_by_city, 'Oakland', checkStatusCode.is_success),
                              (apiClient.get_brewery_by_tag, 'dog-friendly', checkStatusCode.is_success),
                              (apiClient.get_brewery_by_tags, 'dog-friendly, tours', checkStatusCode.is_success),
                              (apiClient.get_brewery_by_type, 'brewpub', checkStatusCode.is_success),
                              (apiClient.get_brewery_page, '1', checkStatusCode.is_success),
                              (apiClient.get_brewery_with_autocomplete, 'dog', checkStatusCode.is_success)])
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
            checkStatusCode.is_success(response)
            print("Brewery for you is found!")
        except AssertionError:
            checkStatusCode.is_not_found(response)
            print("Sorry, brewery with this id doesn't exist")

    def test_brewery_types(self, brewery_types):
        response = apiClient.get_brewery_by_type(brewery_types)
        actual_brewery_type = response.json()[0]['brewery_type']
        assert actual_brewery_type == brewery_types

    def test_brewery_by_tags(self):
        response = apiClient.get_brewery_by_tags('dog-friendly', 'patio')
        checkStatusCode.is_success(response)
