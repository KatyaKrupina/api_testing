import requests


class ApiClientJsonPlaceHolder:

    def __init__(self):
        self.host = 'https://jsonplaceholder.typicode.com/'

    def get_path(self, path):
        return requests.get(self.host + path)

    def post_request(self):
        return requests.post(self.host + 'posts')

    def put_request(self, id):
        return requests.put(self.host + f'posts/{id}')

    def patch_request(self, id):
        return requests.patch(self.host + f'posts/{id}')

    def delete_request(self, id):
        return requests.delete(self.host + f'posts/{id}')

    def get_all_posts(self):
        return self.get_path('posts')

    def get_post_by_id(self, post_id):
        return self.get_path(f'posts/{post_id}')

    def get_comments_from_post_by_id(self, id):
        return self.get_path(f'posts/{id}/comments')

    def get_comments_by_post_id(self, post_id):
        return self.get_path(f'comments?postId={post_id}')

    def get_post_by_user_id(self, user_id):
        return self.get_path(f'posts?userId={user_id}')