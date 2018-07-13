from dimensions_client.doi_input import DOIInputLoader
from dimensions_client.query_builder import QueryBuilder
from dimensions_client.dimensions_request import DimensionsRequest
from dimensions_client.publications_loader import PublicationsLoader
from dimensions_client.output_writer_csv.csv_writer_publication import CSVWriterPublication

import math

class DimensionsClientFacade:

    def __init__(self):

        self.__api_base_uri = None
        self.__api_auth_endpoint = None
        self.__api_dsl_endpoint = None
        self.__api_username = None
        self.__api_password = None
        self.__batch_size = None
        self.__doi_file_input_path = None
        self.__result_output_directory = None
        self.__result_output_base_filename = None

        self.__missing_dois = []
        self.__error_list = []

    @property
    def api_base_uri(self):
        return self.__api_base_uri

    @api_base_uri.setter
    def api_base_uri(self, api_base_uri):
        self.__api_base_uri = api_base_uri

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
    def batch_size(self):
        return self.__batch_size

    @batch_size.setter
    def batch_size(self, batch_size):
        self.__batch_size = batch_size

    @property
    def doi_file_input_path(self):
        return self.__doi_file_input_path

    @doi_file_input_path.setter
    def doi_file_input_path(self, doi_file_input_path):
        self.__doi_file_input_path = doi_file_input_path

    @property
    def result_output_directory(self):
        return self.__result_output_directory

    @result_output_directory.setter
    def result_output_directory(self, result_output_directory):
        self.__result_output_directory = result_output_directory

    @property
    def result_output_basename(self):
        return self.__result_output_base_filename

    @result_output_basename.setter
    def result_output_basename(self, result_output_basename):
        self.__result_output_base_filename = result_output_basename

    @property
    def missing_dois(self):
        return self.__missing_dois

    @property
    def error_list(self):
        return self.__error_list

    def execute(self):

        doi_input_loader = DOIInputLoader(self.__doi_file_input_path)

        batch_count = 0

        try:

            doi_input_loader.load_dois()
            batch_count = math.ceil(float(doi_input_loader.loaded_doi_count) / float(self.__batch_size))
            print("{0} DOIs loaded. {1} batches of DOIs to fetch.".format(doi_input_loader.loaded_doi_count,
                                                                          batch_count))

        except FileNotFoundError:

            print('The DOI input file {0} could not be found'.format(self.__doi_file_input_path))


        query_builder = QueryBuilder()

        dimensions_request = DimensionsRequest(self.__api_base_uri,
                                                self.__api_auth_endpoint,
                                                self.__api_dsl_endpoint,
                                                self.__api_username,
                                                self.__api_password,
                                                query_builder)

        publications_loader = PublicationsLoader()

        csv_writer = CSVWriterPublication("{0}_publications.csv".format(self.__result_output_base_filename),
                                          self.__result_output_directory)

        current_batch_number = 0

        while doi_input_loader.has_next():

            current_batch_number += 1

            print("Fetching batch {0}/{1}".format(current_batch_number, batch_count))

            doi_batch = doi_input_loader.get_next(int(self.__batch_size))

            try:

                data = dimensions_request.request(doi_batch)

                publications = publications_loader.load_publications(data)

                for doi in doi_batch:

                    found_publications = [publication for publication in publications if publication.doi == doi]

                    if len(found_publications) == 0:

                        self.__missing_dois.append(doi)

                csv_writer.publications_list = publications
                csv_writer.write_publications()

            except Exception as ex:

                doi_list = ''

                for doi in doi_batch:

                    doi_list = doi_list + doi + " "

                self.__error_list.append("Error: {0} DOI list: {1}".format(ex, doi_list))

        print('All done!')