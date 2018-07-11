from dimensions_client.publication import Publication

class PublicationsLoader:

    def load_publications(self, publications_data):

        results = []

        for publication_data in publications_data['publications']:

            current_publication = Publication()

            current_publication.doi = publication_data['doi']

            current_publication.title = publication_data['title']

            if 'open_access' in publication_data:

                current_publication.known_to_be_open = True

                if len(publication_data['open_access']) == 2:

                    current_publication.open_access_status = publication_data['open_access'][1]

                elif len(publication_data['open_access']) == 1:

                    current_publication.open_access_status = "Open Access but source unknown"

                else:

                    print('Looks like Dimensions may have changed the Open Access information returned by their API')

            else:

                current_publication.open_access_status = 'NA'


            results.append(current_publication)

        return results