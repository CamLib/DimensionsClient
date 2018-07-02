import configparser
from dimensions_client.dimensions_request import DimensionsRequest
from dimensions_client.query_builder import QueryBuilder

class TestDimensionsRequest:

    def setup_method(self):

        config_data = configparser.ConfigParser()

        # There's a relative path here, so the test will only run (in PyCharm) if the working directory
        # is set properly in the test run configuration.
        # See https://www.jetbrains.com/help/pycharm/run-debug-configuration.html

        with open('../config.ini') as config_file:
            config_data.read_file(config_file)

        api_base_uri = config_data["app.dimensions.ai"]["APIBaseURI"]
        api_auth_endpoint = config_data["app.dimensions.ai"]["APIAuthEndpoint"]
        api_dsl_endpoint = config_data["app.dimensions.ai"]["APIDSLEndpoint"]
        api_username = config_data["app.dimensions.ai"]["APIUsername"]
        api_password = config_data["app.dimensions.ai"]["APIPassword"]

        query_builder = QueryBuilder()

        self.__test_request = DimensionsRequest(api_base_uri,
                                                api_auth_endpoint,
                                                api_dsl_endpoint,
                                                api_username,
                                                api_password,
                                                query_builder)

    def test_base_url_property(self):

        self.__test_request.api_url = 'http://test/url/endpoint'

        assert self.__test_request.api_url == 'http://test/url/endpoint'

    def test_auth_endpoint(self):

        self.__test_request.api_auth_endpoint = 'test_auth_endpoint'

        assert self.__test_request.api_auth_endpoint == 'test_auth_endpoint'

    def test_dsl_endpoint(self):

        self.__test_request.api_dsl_endpoint = 'test_dsl_endpoint'

        assert self.__test_request.api_dsl_endpoint == 'test_dsl_endpoint'

    def test_username_property(self):

        self.__test_request.api_username = 'test_username'

        assert self.__test_request.api_username == 'test_username'

    def test_password_property(self):

        self.__test_request.api_password = 'test_password'

        assert self.__test_request.api_password == 'test_password'


    def test_login_token_returned(self):

        assert self.__test_request.login_token is not None

    def test_single_doi(self):

        test_single_doi = ["10.2218/ijdc.v8i1.242"]

        result = self.__test_request.request(test_single_doi)

        assert result["publications"][0]["title"] == "Competencies Required for Digital Curation: An Analysis of Job Advertisements"