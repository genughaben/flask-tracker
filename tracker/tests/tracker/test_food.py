

class TestFood():

    def test_home_page(self, client):
        """ Home page should respond with a success 200. """
        response = client.get('/')
        assert response.status_code == 200
