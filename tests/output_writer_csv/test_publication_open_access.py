from dimensions_client.output_writer_csv.csv_writer_publication import CSVWriterPublication
from dimensions_client.publication import Publication
from csv import DictReader

import os

class TestPublicationOpenAccessOutput:

    def setup_method(self):

        self._test_file_name = 'test_publication_output.csv'
        self._files_out_directory = '../files_out/'

        # clean up the old test file in the setup

        filepath = '{0}{1}'.format(self._files_out_directory, self._test_file_name)

        if os.path.isfile(filepath):
            os.remove(filepath)

        self.__test_publication_list = []

        pub1 = Publication()
        pub1.doi = 'test/doi/01'
        pub1.title = 'Test title 1'
        pub1.open_access_status = "Open Access in repository"
        pub1.known_to_be_open = True

        self.__test_publication_list.append(pub1)

        pub2 = Publication()
        pub2.doi = 'test/doi/02'
        pub2.title = 'Test title 2'
        pub2.open_access_status = "NA"
        pub2.known_to_be_open = False

        self.__test_publication_list.append(pub2)

        self.__test_csv_writer_publication = CSVWriterPublication(self._test_file_name, self._files_out_directory)

    def tear_down_method(self):

        self.__test_csv_writer_publication = None

    def test_file_name_added(self):

        self.__test_csv_writer_publication.output_file_name = 'Test Output File Name'
        assert 'Test Output File Name' == self.__test_csv_writer_publication.output_file_name

    def test_directory_name_added(self):

        self.__test_csv_writer_publication.output_directory_name = 'Test Output Dir Name'
        assert 'Test Output Dir Name' == self.__test_csv_writer_publication.output_directory_name

    def test_file_created_with_header_containing_doi(self):

        self.__test_csv_writer_publication.publications_list = self.__test_publication_list

        self.__test_csv_writer_publication.write_publications()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)
            assert test_output_reader.fieldnames[0] == 'doi'

    def test_first_file_doi_written(self):

        self.__test_csv_writer_publication.publications_list = self.__test_publication_list

        self.__test_csv_writer_publication.write_publications()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)
            assert next(test_output_reader)['doi'] == 'test/doi/01'

    def test_first_file_title_written(self):

        self.__test_csv_writer_publication.publications_list = self.__test_publication_list

        self.__test_csv_writer_publication.write_publications()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)
            assert next(test_output_reader)['title'] == 'Test title 1'

    def test_first_file_known_to_be_open_is_true(self):

        self.__test_csv_writer_publication.publications_list = self.__test_publication_list

        self.__test_csv_writer_publication.write_publications()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)
            assert next(test_output_reader)['known_to_be_open'] == 'TRUE'

    def test_first_file_open_access_status(self):

        self.__test_csv_writer_publication.publications_list = self.__test_publication_list

        self.__test_csv_writer_publication.write_publications()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)
            assert next(test_output_reader)['open_access_status'] == 'Open Access in repository'

    def test_second_file_known_to_be_open_is_true(self):

        self.__test_csv_writer_publication.publications_list = self.__test_publication_list

        self.__test_csv_writer_publication.write_publications()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)
            next(test_output_reader)
            assert next(test_output_reader)['known_to_be_open'] == 'FALSE'

    def test_first_file_in_second_list_title(self):

        self.__test_csv_writer_publication.publications_list = self.__test_publication_list
        self.__test_csv_writer_publication.write_publications()

        second_pub_list = []

        pub3 = Publication()
        pub3.doi = 'test/doi/3'
        pub3.title = 'Test title 3'
        pub3.known_to_be_open = True
        pub3.open_access_status = 'Open Access but location unknown'

        second_pub_list.append(pub3)

        self.__test_csv_writer_publication.publications_list = second_pub_list
        self.__test_csv_writer_publication.write_publications()

        with open('{0}{1}'.format(self._files_out_directory, self._test_file_name)) as test_output_csv:

            test_output_reader = DictReader(test_output_csv)
            next(test_output_reader)
            next(test_output_reader)
            assert next(test_output_reader)['known_to_be_open'] == 'TRUE'