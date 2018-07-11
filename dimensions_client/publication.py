class Publication:

    def __init__(self):

        self.__doi = None
        self.__title = None
        self.__known_to_be_open = False
        self.__open_access_status = None

    @property
    def doi(self):
        return self.__doi

    @doi.setter
    def doi(self, doi):
        self.__doi = doi

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def known_to_be_open(self):
        return self.__known_to_be_open

    @known_to_be_open.setter
    def known_to_be_open(self, known_to_be_open):
        self.__known_to_be_open = known_to_be_open

    @property
    def open_access_status(self):
        return self.__open_access_status

    @open_access_status.setter
    def open_access_status(self, open_access_status):
        self.__open_access_status = open_access_status