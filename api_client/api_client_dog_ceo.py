import requests


class ApiClientDog:

    def __init__(self):
        self.host = 'https://dog.ceo/api/breed'

    def add_path(self, path):
        return requests.get(self.host + path)

    def get_brewery_by_id(self, brewery_id):
        return self.add_path(f'/{brewery_id}')

    def get_list_all_breeds(self):
        return self.add_path('s/list/all')

    def get_random_image(self):
        return self.add_path('s/image/random')

    def get_all_images_by_breed(self, breed):
        return self.add_path(f'/{breed}/images')

    def get_random_image_by_breed(self, breed):
        return self.add_path(f'/{breed}/images/random')

    def get_all_sub_breeds(self, breed):
        return self.add_path(f'/{breed}/list')

    def get_all_sub_breeds_images(self, breed, sub_breed):
        return self.add_path(f'/{breed}/{sub_breed}/images')

    def get_list_with_error(self):
        return self.add_path('/list')
