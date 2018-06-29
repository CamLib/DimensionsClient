from dimensions_client.doi_input import DOIInputLoader

class TestDOIInputFileReader:

    def setup_method(self):

        self.__test_input_loader = DOIInputLoader('../files_in/test_dois.csv')
        self.__test_input_loader.load_dois()

    def test_file_path_loaded(self):

        assert self.__test_input_loader.input_file_path == "../files_in/test_dois.csv"

    def test_files_loaded(self):

        assert self.__test_input_loader.loaded_doi_count == 23

    def test_get_first_five_returns_list_of_five(self):

        result = self.__test_input_loader.get_next(5)

        assert len(result) == 5

    def test_get_first_five_returns_correct_first_doi(self):

        result = self.__test_input_loader.get_next(5)

        assert result[0] == '10.1001/jama.2013.950'

    def test_get_first_five_returns_correct_last_doi(self):

        result = self.__test_input_loader.get_next(5)

        assert result[4] == '10.2218/ijdc.v8i1.242'

    def test_get_second_five_returns_correct_first_doi(self):

        first_five = self.__test_input_loader.get_next(5)
        result = self.__test_input_loader.get_next(5)

        assert result[0] == '10.1186/2041-1480-5-25'

    def test_get_second_five_returns_correct_first_doi(self):

        first_five = self.__test_input_loader.get_next(5)
        result = self.__test_input_loader.get_next(5)

        assert result[4] == '10.2196/jmir.7463'

    def test_get_the_last_three(self):

        result = None

        while self.__test_input_loader.has_next():

            result = self.__test_input_loader.get_next(5)

        assert len(result) == 3

    def test_first_doi_of_the_last_three(self):

        result = None

        while self.__test_input_loader.has_next():

            result = self.__test_input_loader.get_next(5)

        assert result[0] == "10.1080/19322909.2012.729992"

    def test_last_doi_of_the_last_three(self):

        result = None

        while self.__test_input_loader.has_next():

            result = self.__test_input_loader.get_next(5)

        assert result[2] == "10.1093/ohr/oht035"

