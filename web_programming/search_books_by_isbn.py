import requests

URL_BASE = "https://openlibrary.org"

def get_book_by_isbn(isbn: str = "0140328726") -> dict:
    """
    Given a isbn code, return a dict.

    :param isbn: string
    :return: dict

    >>> get_book_by_isbn('0140328726')
    {'publishers': ['Puffin'], 'number_of_pages': 96, 'isbn_10': ['0140328726'], 'covers': [8739161], 'key': '/books/OL7353617M', 'authors': [{'key': '/authors/OL34184A'}], 'ocaid': 'fantasticmrfoxpu00roal', 'contributions': ['Tony Ross (Illustrator)'], 'languages': [{'key': '/languages/eng'}], 'classifications': {}, 'source_records': ['ia:fantasticmrfox00dahl_834', 'marc:marc_openlibraries_sanfranciscopubliclibrary/sfpl_chq_2018_12_24_run02.mrc:85081404:4525'], 'title': 'Fantastic Mr. Fox', 'identifiers': {'goodreads': ['1507552'], 'librarything': ['6446']}, 'isbn_13': ['9780140328721'], 'local_id': ['urn:sfpl:31223064402481', 'urn:sfpl:31223117624784', 'urn:sfpl:31223113969183', 'urn:sfpl:31223117624800', 'urn:sfpl:31223113969225', 'urn:sfpl:31223106484539', 'urn:sfpl:31223117624792', 'urn:sfpl:31223117624818', 'urn:sfpl:31223117624768', 'urn:sfpl:31223117624743', 'urn:sfpl:31223113969209', 'urn:sfpl:31223117624750', 'urn:sfpl:31223117624727', 'urn:sfpl:31223117624776', 'urn:sfpl:31223117624719', 'urn:sfpl:31223117624735', 'urn:sfpl:31223113969241'], 'publish_date': 'October 1, 1988', 'works': [{'key': '/works/OL45883W'}], 'type': {'key': '/type/edition'}, 'first_sentence': {'type': '/type/text', 'value': 'And these two very old people are the father and mother of Mrs. Bucket.'}, 'latest_revision': 14, 'revision': 14, 'created': {'type': '/type/datetime', 'value': '2008-04-29T13:35:46.876380'}, 'last_modified': {'type': '/type/datetime', 'value': '2021-06-18T22:46:46.648233'}}
    """

    url = URL_BASE + "/isbn/" + isbn + ".json"
    return requests.get(url, params=locals()).json()

def get_author(author_url: str = "/authors/OL34184A") -> dict:
    """
    Given a valid url, return a dict.

    :param author_url: string
    :return: dict

    >>> get_author('/authors/OL7353617A')
    {'name': 'Adrian Brisku', 'created': {'type': '/type/datetime', 'value': '2016-10-19T02:33:46.926858'}, 'last_modified': {'type': '/type/datetime', 'value': '2016-10-19T02:33:46.926858'}, 'latest_revision': 1, 'key': '/authors/OL7353617A', 'type': {'key': '/type/author'}, 'revision': 1}
    """

    url = URL_BASE + author_url + ".json"
    return requests.get(url, params=locals()).json()

if __name__ == "__main__":

    import doctest
    doctest.testmod()

    while True:
        book = input("\nEnter the ISBN code to search (or CTRL+C to stop): ").strip()

        if book.isnumeric() and (len(book) == 10 or len(book) == 13):

            print("\nSearching...\n")

            result = get_book_by_isbn(book)

            keys = result.keys()
            keys_title = {
                'title': 'Title',
                'publish_date': 'Publish date',
                'authors': 'Authors',
                'number_of_pages': 'Number of pages:',
                'first_sentence': 'First sentence',
                'isbn_10': 'ISBN (10)',
                'isbn_13': 'ISBN (13)'
            }

            if result:

                print("\nLoading...\n")

                authors = []

                for author in result['authors']:
                    partial_result = get_author(author['key'])
                    authors.append(partial_result['name'])

                ",".join(authors)

                for key in keys_title.keys():
                    if (key in result.keys()):
                        if (key == 'first_sentence'):     
                            print(keys_title[key], ": ", str(result[key]['value']).strip('[]'))
                        elif (key == 'authors'):
                            print(keys_title[key], ": ", str(authors).strip('[]'))
                        else:
                            print(keys_title[key], ": ", str(result[key]).strip('[]'))
            
            else:
                print("Sorry, there are no results for this search")
        else:
            print("Sorry, not a valid ISBN, please, inform some valid code")
            break
