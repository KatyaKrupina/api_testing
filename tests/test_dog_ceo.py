import pytest
from jsonschema import validate

from api_client.api_client_dog_ceo import ApiClientDog
from utils import CheckStatusCode

checkStatusCode = CheckStatusCode()
apiClient = ApiClientDog()


@pytest.mark.parametrize('method, check',
                         [(apiClient.get_list_all_breeds, checkStatusCode.isSuccess),
                          (apiClient.get_random_image, checkStatusCode.isSuccess),
                          (apiClient.get_list_with_error, checkStatusCode.isClientError)])
def test_status_code(method, check):
    response = method()
    check(response)


@pytest.mark.parametrize('breed', ['Boxer', 'Clumber', 'Shiba'])
def test_breed_image(all_breeds_schema, breed):
    response = apiClient.get_random_image_by_breed(breed=breed)
    schema = all_breeds_schema
    validate(instance=response.json(), schema=schema)


@pytest.mark.parametrize('breed', ['hound', 'cockapoo', 'pointer'])
def test_sub_breeds_images(breed):
    response = apiClient.get_all_sub_breeds(breed=breed)
    sub_breeds = response.json()['message']
    if not sub_breeds:
        print("This breed doesn't have sub_breeds")
    else:
        for sub_breed in sub_breeds:
            response = apiClient.get_all_sub_breeds_images(breed=breed, sub_breed=sub_breed)
            checkStatusCode.isSuccess(response)


def test_response_all_breeds_ok():
    response = apiClient.get_list_all_breeds()
    all_breeds = response.json()
    dogs = all_breeds['message']
    for breed in dogs.keys():
        res = apiClient.get_random_image_by_breed(breed=breed)
        checkStatusCode.isSuccess(res)


def test_all_sub_breeds_type():
    response = apiClient.get_all_sub_breeds(breed='hound')
    sub_breeds_list = response.json()['message']
    assert type(sub_breeds_list) == list
