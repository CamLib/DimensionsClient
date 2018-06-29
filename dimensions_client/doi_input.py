from csv import DictReader

class DOIInputLoader:

    def __init__(self, input_file_path = None):

        self.__input_file_path = input_file_path
        self.__doi_list = []
        self.__start_point = 0

    @property
    def input_file_path(self):
        return self.__input_file_path

    @input_file_path.setter
    def input_file_path(self, file_path):
        self.__input_file_path = file_path

    @property
    def loaded_doi_count(self):
        return len(self.__doi_list)

    def load_dois(self):

        try:

            with open(self.__input_file_path, 'r') as doi_input_csv:

                doi_input_reader = DictReader(doi_input_csv)

                for doi_row in doi_input_reader:

                    self.__doi_list.append(doi_row['DOI'])

        except FileNotFoundError:

            print("Could not find the input file at the location: {0}".format(self.input_file_path))

        except Exception as ex:

            print("The input file was found OK, but something weird happened when loading it.")
            print('The error was: {0}'.format(ex))

    def get_next(self, result_size):

        result = self.__doi_list[self.__start_point:self.__start_point + result_size]

        self.__start_point += result_size

        return result

    def has_next(self):

        return (self.loaded_doi_count - self.__start_point) > 0
