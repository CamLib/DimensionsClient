from dimensions_client.output_writer_csv.csv_writer_base import CSVWriterBase
from csv import DictWriter

class CSVWriterPublication(CSVWriterBase):

    def __init__(self,
                 output_file_name=None,
                 output_directory_name=None,
                 publications_list = None):

        CSVWriterBase.__init__(self, output_file_name, output_directory_name)

        self.__publications_list = publications_list

    @property
    def publications_list(self):
        return self.__publications_list

    @publications_list.setter
    def publications_list(self, publications_list):
        self.__publications_list = publications_list

    def write_publications(self):

        output_file_path = '{0}{1}'.format(self.output_directory_name, self.output_file_name)

        write_mode = self._get_write_mode(output_file_path)

        fieldnames = ['doi', 'title', 'known_to_be_open', 'open_access_status']

        try:

            with open(output_file_path, write_mode) as output_csv:

                output_writer = DictWriter(output_csv, fieldnames=fieldnames)

                if write_mode == 'w':

                    output_writer.writeheader()

                for publication in self.__publications_list:

                    output_dict = dict(doi=publication.doi,
                                       title=publication.title,
                                       known_to_be_open=str(publication.known_to_be_open).upper(),
                                       open_access_status=publication.open_access_status)

                    output_writer.writerow(output_dict)

        except:

            print('Something totally unexpected happened when trying to write to a Publications CSV file')
            print('The writer was setup to write to a file called {0}{1}'.format(self.output_directory_name,
                                                                                 self.output_file_name))
            if write_mode == 'a':
                print('The writer thought this file existed and was trying to append to it.')
            elif write_mode == 'w':

                print('The writer thought this was a brand new file and was trying to create it.')
            else:
                print('The writer could not determine whether or not the file existed.')

