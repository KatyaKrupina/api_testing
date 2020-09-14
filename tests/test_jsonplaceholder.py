import random
import pytest

from api_client.api_client_jsonplaceholder import ApiClientJsonPlaceHolder
from utils import CheckStatusCode

checkStatusCode = CheckStatusCode()
apiClient = ApiClientJsonPlaceHolder()


class TestJsonPlaceHolder:
    @pytest.mark.parametrize('method, check',
                             [(apiClient.post_request, checkStatusCode.is_created),
                              (apiClient.get_all_posts, checkStatusCode.is_success)])
    def test_status_code(self, method, check):
        response = method()
        check(response)

    @pytest.mark.parametrize('method, param, check',
                             [(apiClient.get_comments_by_post_id, '1', checkStatusCode.is_success),
                              (apiClient.get_comments_from_post_by_id, '2', checkStatusCode.is_success),
                              (apiClient.get_comments_by_post_id, '3', checkStatusCode.is_success),
                              (apiClient.get_post_by_id, '4', checkStatusCode.is_success),
                              (apiClient.get_post_by_user_id, '5', checkStatusCode.is_success),
                              (apiClient.put_request, '6', checkStatusCode.is_success),
                              (apiClient.patch_request, '7', checkStatusCode.is_success),
                              (apiClient.delete_request, '8', checkStatusCode.is_success)])
    def test_status_code_all_requests(self, method, param, check):
        response = method(param)
        check(response)

    def test_get_random_post_title(self):
        random_id = str(random.randint(1, 100))
        response = apiClient.get_post_by_id(random_id)
        post_title = response.json()['title']
        assert type(post_title) == str

    def test_get_commentators_names(self):
        response = apiClient.get_comments_by_post_id('5')
        checkStatusCode.is_success(response)
        comments = response.json()
        comments_quantity = len(response.json())
        for i in range(comments_quantity):
            print(comments[i]['name'])

    def test_new_post(self):
        response = apiClient.post_request()
        checkStatusCode.is_created(response)
        new_id = response.json()['id']
        assert new_id == 101
