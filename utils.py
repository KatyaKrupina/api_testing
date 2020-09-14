class CheckStatusCode:
    def is_success(self, response):
        assert response.status_code == 200

    def is_created(self, response):
        assert response.status_code == 201

    def is_not_found(self, response):
        assert response.status_code == 404
