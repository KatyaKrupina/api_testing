import random
import pytest


@pytest.fixture
def all_breeds_schema():
    schema = {"message": "url", "status": "success"}
    return schema


@pytest.fixture()
def random_fixture():
    return str(random.randint(1, 15000))


@pytest.fixture
def brewery_schema():
    schema = {
                "id": int,
                "name": "string",
                "brewery_type": "string",
                "street": "string",
                "city": "string",
                "state": "string",
                "postal_code": "number",
                "country": "string",
                "longitude": "number",
                "latitude": "number",
                "phone": "number",
                "website_url": "url",
                "updated_at": "number",
                "tag_list": list
            }
    return schema


@pytest.fixture(params=
                ['micro',
                 'regional',
                 'brewpub',
                 'large',
                 'planning',
                 'bar',
                 'contract',
                 'proprietor'])
def brewery_types(request):
    return request.param
