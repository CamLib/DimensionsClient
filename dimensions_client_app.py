from dimensions_client.dimensions_client_facade import DimensionsClientFacade

import configparser

class DimensionsClient:

    def run(self):

        config_data = configparser.ConfigParser()

        with open('config.ini') as config_file:
            config_data.read_file(config_file)

        input_dir = input('Enter an input directory (with trailing slash):')
        input_file = input('Enter the DOI list input file name:')
        output_dir = input('Enter an output directory (with trailing slash):')
        output_files_root = input('Enter the name root for the output files (e.g. "19720315_0830" for "19720315_0830_master.csv" etc):')

        dimensions_client_facade = DimensionsClientFacade()

        dimensions_client_facade.api_base_uri = config_data["app.dimensions.ai"]["APIBaseURI"]
        dimensions_client_facade.api_auth_endpoint = config_data["app.dimensions.ai"]["APIAuthEndpoint"]
        dimensions_client_facade.api_dsl_endpoint = config_data["app.dimensions.ai"]["APIDSLEndpoint"]
        dimensions_client_facade.api_username = config_data["app.dimensions.ai"]["APIUsername"]
        dimensions_client_facade.api_password = config_data["app.dimensions.ai"]["APIPassword"]
        dimensions_client_facade.batch_size = config_data["app.dimensions.ai"]["DOIBatchSize"]
        dimensions_client_facade.doi_file_input_path = "{0}{1}".format(input_dir, input_file)
        dimensions_client_facade.result_output_directory = output_dir
        dimensions_client_facade.result_output_basename = output_files_root

        dimensions_client_facade.execute()

        if len(dimensions_client_facade.missing_dois) == 0:

            print("All the DOIs in the input file were successfully retrieved.")

        else:

            print("The following DOIs were missing:")

            for missing_doi in dimensions_client_facade.missing_dois:

                print(missing_doi)

        if len(dimensions_client_facade.error_list) == 0:

            print("No errors occurred.")

        else:

            print("The following errors occurred:")

            for error in dimensions_client_facade.error_list:

                print(error)


if __name__ == "__main__":

    DimensionsClient().run()