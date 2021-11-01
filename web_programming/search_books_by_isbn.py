import requests

URL_BASE = "https://openlibrary.org"

def get_book_by_isbn(isbn: str = "0140328726") -> dict:
    url = URL_BASE + "/isbn/" + isbn + ".json"
    return requests.get(url, params=locals()).json()

def get_author(author_url: str = "/authors/OL34184A") -> dict:
    url = URL_BASE + author_url + ".json"
    return requests.get(url, params=locals()).json()

if __name__ == "__main__":

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
