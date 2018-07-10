from dimensions_client.publications_loader import PublicationsLoader

import json

class TestPublicationsLoader:

    def setup_method(self):

        self.__test_publications_loader = PublicationsLoader()

    def test_one_result(self):

        one_result_file = open('../files_in/one_result.json')

        one_result_data = json.load(one_result_file)

        results = self.__test_publications_loader.load_publications(one_result_data)

        one_result_file.close()

        assert results[0].is_open == True

    def test_one_result_doi(self):

        one_result_file = open('../files_in/one_result.json')

        one_result_data = json.load(one_result_file)

        results = self.__test_publications_loader.load_publications(one_result_data)

        one_result_file.close()

        assert results[0].doi == "10.1001/jama.2013.950"

    def test_one_result_doi(self):

        one_result_file = open('../files_in/one_result.json')

        one_result_data = json.load(one_result_file)

        results = self.__test_publications_loader.load_publications(one_result_data)

        one_result_file.close()

        assert results[0].title == "Surveillance Intervals for Small Abdominal Aortic Aneurysms: A Meta-analysis"


    def test_two_open_results(self):

        two_open_result_file = open('../files_in/two_open.json')

        two_open_result_data = json.load(two_open_result_file)

        results = self.__test_publications_loader.load_publications(two_open_result_data)

        two_open_result_file.close()

        assert results[1].is_open == True

    def test_two_closed_results(self):

        two_closed_result_file = open('../files_in/two_closed.json')

        two_closed_result_data = json.load(two_closed_result_file)

        results = self.__test_publications_loader.load_publications(two_closed_result_data)

        two_closed_result_file.close()

        assert results[1].is_open == False

    def test_ten_results_have_seven_open(self):

        ten_result_file = open('../files_in/ten_results.json')

        ten_result_data = json.load(ten_result_file)

        results = self.__test_publications_loader.load_publications(ten_result_data)

        ten_result_file.close()

        filtered_results = [open_results for open_results in results if open_results.is_open]

        assert len(filtered_results) == 7

    def test_twenty_results_have_six_closed(self):

        twenty_result_file = open('../files_in/twenty_results.json')

        twenty_result_data = json.load(twenty_result_file)

        results = self.__test_publications_loader.load_publications(twenty_result_data)

        twenty_result_file.close()

        filtered_results = [open_results for open_results in results if not open_results.is_open]

        assert len(filtered_results) == 6

