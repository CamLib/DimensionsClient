import requests
import json
from dimensions_client.query_builder import QueryBuilder

class DimensionsRequest:

    def __init__(self,
                 api_url,
                 api_auth_endpoint,
                 api_dsl_endpoint,
                 api_username,
                 api_password,
                 query_builder: QueryBuilder):

        self.__api_url = api_url
        self.__api_auth_endpoint = api_auth_endpoint
        self.__api_dsl_endpoint = api_dsl_endpoint
        self.__api_username = api_username
        self.__api_password = api_password
        self.__query_builder = query_builder

        self.__login_token = self.__login()

    @property
    def api_url(self):
        return self.__api_url

    @api_url.setter
    def api_url(self, api_url):
        self.__api_url = api_url

    @property
    def api_auth_endpoint(self):
        return self.__api_auth_endpoint

    @api_auth_endpoint.setter
    def api_auth_endpoint(self, api_auth_endpoint):
        self.__api_auth_endpoint = api_auth_endpoint

    @property
    def api_dsl_endpoint(self):
        return self.__api_dsl_endpoint

    @api_dsl_endpoint.setter
    def api_dsl_endpoint(self, api_dsl_endpoint):
        self.__api_dsl_endpoint = api_dsl_endpoint

    @property
    def api_username(self):
        return self.__api_username

    @api_username.setter
    def api_username(self, api_username):
        self.__api_username = api_username

    @property
    def api_password(self):
        return self.__api_password

    @api_password.setter
    def api_password(self, api_password):
        self.__api_password = api_password

    @property
    def query_builder(self):
        return self.__query_builder

    @query_builder.setter
    def query_builder(self, query_builder: QueryBuilder):
        self.__query_builder = query_builder

    @property
    def login_token(self):
        return self.__login_token

    def __login(self):

        login = {
            'username': self.__api_username,
            'password': self.__api_password
        }

        auth_endpoint = "{0}{1}".format(self.__api_url, self.__api_auth_endpoint)

        result = None

        try:

            resp = requests.post(auth_endpoint, json=login)
            resp.raise_for_status()

            result = resp.json()["token"]

        except ConnectionError:

            print("Could not connect to the API endpoint {0}".format(auth_endpoint))
            result = 'Login failed due to connection error'

        except TimeoutError:

            print("The response timed out when calling the API endpoint {0}".format(auth_endpoint))
            result = 'Login failed due to timeout'

        except requests.exceptions.RequestException as reqEx:

            print("A Request Exception occurred. Error was: {0}".format(reqEx))
            result = 'Login failed due to Request Exception'

        except Exception as ex:

            print("Something totally unexpected happened. Error was: {0}".format(ex))
            result = 'Login failed due to unexpected general exception'

        return result

    def request(self, doi_list):

        #   Create http header using the generated token.
        headers = {
            'Authorization': "JWT " + self.__login_token
        }

        self.__query_builder.dois = doi_list

        dsl_endpoint = '{0}{1}'.format(self.__api_url, self.__api_dsl_endpoint)

        result = None

        try:

            #   Execute DSL query.
            resp = requests.post(
                dsl_endpoint,
                data=self.__query_builder.build_query(),
                headers=headers)

            result = resp.json()

        except ConnectionError:

            print("Could not connect to the API endpoint {0}".format(dsl_endpoint))
            result = 'Data retrieval failed due to connection error'

        except TimeoutError:

            print("The response timed out when calling the API endpoint {0}".format(dsl_endpoint))
            result = 'Data retrieval failed due to timeout'

        except requests.exceptions.RequestException as reqEx:

            print("A Request Exception occurred. Error was: {0}".format(reqEx))
            result = 'Data retrieval failed due to Request Exception'

        except Exception as ex:

            print("Something totally unexpected happened. Error was: {0}".format(ex))
            result = 'Data retrieval failed due to unexpected general exception'

        return result
