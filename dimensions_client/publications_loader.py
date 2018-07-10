from dimensions_client.publication import Publication

class PublicationsLoader:

    def load_publications(self, publications_data):

        results = []

        for publication_data in publications_data['publications']:

            current_publication = Publication()

            current_publication.doi = publication_data['doi']

            current_publication.title = publication_data['title']

            if 'open_access' in publication_data:

                current_publication.is_open = True

            results.append(current_publication)

        return results