class QueryBuilder:

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


