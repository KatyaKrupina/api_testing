class CheckStatusCode:
    def isSuccess(self, response):
        assert response.status_code == 200

    def isCreated(self, response):
        assert response.status_code == 201

    def isClientError(self, response):
        assert response.status_code == 404
