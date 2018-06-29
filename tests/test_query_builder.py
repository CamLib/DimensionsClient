from dimensions_client.query_builder import QueryBuilder

class TestQueryBuilder:

    def setup_method(self):

        self.__test_query_builder = QueryBuilder()

    def test_one_doi(self):

        test_dois = ["test/doi/1"]
        self.__test_query_builder.dois = test_dois

        assert self.__test_query_builder.build_query() == 'search publications where doi="test/doi/1" ' \
                                                          'return publications [doi + title + open_access]'

    def test_two_dois(self):

        test_dois = ["test/doi/1", "test/doi/2"]
        self.__test_query_builder.dois = test_dois

        assert self.__test_query_builder.build_query() == 'search publications where doi="test/doi/1" ' \
                                                          'or doi="test/doi/2" ' \
                                                          'return publications [doi + title + open_access]'

    def test_three_dois(self):

        test_dois = ["test/doi/1", "test/doi/2", "test/doi/3"]
        self.__test_query_builder.dois = test_dois

        assert self.__test_query_builder.build_query() == 'search publications where doi="test/doi/1" ' \
                                                          'or doi="test/doi/2" ' \
                                                          'or doi="test/doi/3" ' \
                                                          'return publications [doi + title + open_access]'

