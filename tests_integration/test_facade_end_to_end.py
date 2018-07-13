from dimensions_client.dimensions_client_facade import DimensionsClientFacade
from csv import DictReader

import configparser
import os


class TestFacadeEndToEnd:

    @classmethod
    def setup_class(self):

        # Setup test file names and paths
        # Relative paths are used here, so the test will only run (in PyCharm) if the working directory
        # is set properly in the test run configuration.
        # See https://www.jetbrains.com/help/pycharm/run-debug-configuration.html

        _test_output_name_root = 'test_bare_minimum_end_to_end'
        _files_out_directory = '../files_out/'

        # Delete the pre-existing output files if they are there

        publications_filepath = '{0}{1}_publications.csv'.format(_files_out_directory, _test_output_name_root)

        if os.path.isfile(publications_filepath):
            os.remove(publications_filepath)

        # Pass the api url, endpoints, login details and path to the test doi file

        config_data = configparser.ConfigParser()

        # There's a relative path here, so the test will only run (in PyCharm) if the working directory
        # is set properly in the test run configuration.
        # See https://www.jetbrains.com/help/pycharm/run-debug-configuration.html

        with open('../config.ini') as config_file:
            config_data.read_file(config_file)

        self.__test_dimensions_client_facade = DimensionsClientFacade()

        self.__test_dimensions_client_facade.api_base_uri = config_data["app.dimensions.ai"]["APIBaseURI"]
        self.__test_dimensions_client_facade.api_auth_endpoint = config_data["app.dimensions.ai"]["APIAuthEndpoint"]
        self.__test_dimensions_client_facade.api_dsl_endpoint = config_data["app.dimensions.ai"]["APIDSLEndpoint"]
        self.__test_dimensions_client_facade.api_username = config_data["app.dimensions.ai"]["APIUsername"]
        self.__test_dimensions_client_facade.api_password = config_data["app.dimensions.ai"]["APIPassword"]
        self.__test_dimensions_client_facade.batch_size = config_data["app.dimensions.ai"]["DOIBatchSize"]
        self.__test_dimensions_client_facade.doi_file_input_path = '../files_in/test_dois.csv'
        self.__test_dimensions_client_facade.result_output_directory = _files_out_directory
        self.__test_dimensions_client_facade.result_output_basename = _test_output_name_root

        self.__test_dimensions_client_facade.execute()

    def setup_method(self):

        self._test_publications_output_file_path = '../files_out/test_bare_minimum_end_to_end_publications.csv'

    def test_csv_writing_end_to_end_writes_publication_doi(self):

        with open(self._test_publications_output_file_path) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)

            for row in test_output_reader:

                if row['doi'] == '10.1001/jama.2013.950':

                    assert row['title'] == 'Surveillance Intervals for Small Abdominal Aortic Aneurysms: A Meta-analysis'

    def test_missing_doi(self):

        assert self.__test_dimensions_client_facade.missing_dois[0] == '666.999/test_missing_doi'

