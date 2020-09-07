import requests


class ApiClientBreweries:

    def __init__(self):
        self.host = 'https://api.openbrewerydb.org/breweries'

    def add_path(self, path):
        return requests.get(self.host + path)

    def get_list_all_breweries(self):
        return self.add_path('')

    def get_brewery_by_id(self, brewery_id):
        return self.add_path(f'/{brewery_id}')

    def get_brewery_by_city(self, city):
        return self.add_path(f'?by_city={city}')

    def get_brewery_by_name(self, name):
        return self.add_path(f'?by_name={name}')

    def get_brewery_by_state(self, state):
        return self.add_path(f'?by_state={state}')

    def get_brewery_by_postal(self, postal):
        return self.add_path(f'?by_postal={postal}')

    def get_brewery_by_type(self, brewery_type):
        return self.add_path(f'?by_type={brewery_type}')

    def get_brewery_by_tag(self, tag):
        return self.add_path(f'?by_tag={tag}')

    def get_brewery_by_tags(self, *tags):
        return self.add_path(f'?by_tags={tags}')

    def get_brewery_page(self, page):
        return self.add_path(f'?by_tags={page}')

    def get_brewery_with_autocomplete(self, parameter):
        return self.add_path(f'/autocomplete?query{parameter}')
