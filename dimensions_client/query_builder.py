class QueryBuilder:

    """ Creates the query string to send to Dimensions, using their Domain Specific Language.

    You can test the DSL here: https://app.dimensions.ai/dsl .
    It is documented here: http://docs.dimensions.ai/dsl/1.5.0/

    At present, for the bare-minimum release, the query searches publications by DOI, using an
    or modifier to search for multiple publications. Only the doi, title and open_access fields are
    returned. Only the open_access field is required for our initial research, but we shall use
    the other two for testing / reconciliation purposes.

    This class could become a place where the Dimensions API client could be comprehensively extended,
    behaviours added to search different entities, in different ways, and return all sorts of different
    fields. Hence finding a pattern (like a Decorator or something) to make it easier to extend in
    future might be a worthwhile exercise in the next release beyond the bare minimum.

    """

    def __init__(self, dois = None):

        self.__dois = dois

    @property
    def dois(self):
        return self.__dois

    @dois.setter
    def dois(self, dois):
        self.__dois = dois

    def build_query(self):

        return 'search publications where {0} return publications [doi + title + open_access]'\
            .format(self.__build_doi_section())

    def __build_doi_section(self):

        doi_section = 'doi="{0}"'.format(self.__dois[0])

        if len(self.__dois) > 1:

            remaining_dois = self.__dois[1:len(self.__dois)]

            for doi in remaining_dois:

                doi_section = doi_section + ' or doi="{0}"'.format(doi)

        return doi_section


