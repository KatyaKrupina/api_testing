import random

import pytest


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="http://ya.ru",
        help="This is request url"
    )
    parser.addoption(
        "--status_code",
        default=200,
        help=""
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def code(request):
    return int(request.config.getoption("--status_code"))


@pytest.fixture
def all_breeds_schema():
    schema = {"message": "url", "status": "success"}
    return schema


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


@pytest.fixture()
def random_fixture():
    return str(random.randint(1, 15000))


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

