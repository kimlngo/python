import requests
import bs4

BASE_URL = 'https://quotes.toscrape.com/page/{}/'

def get_quote_url(page_number):
    return BASE_URL.format(page_number)

def get_quote_page(page_number=1):
    quote_page = requests.get(get_quote_url(page_number))
    soup = bs4.BeautifulSoup(quote_page.text, 'lxml')
    print(type(soup))
    return soup

def get_all_authors(page_number=1):
    soup = get_quote_page(page_number)

    return get_authors_from_soup(soup)

def get_authors_from_soup(soup: bs4.BeautifulSoup):
    authors = set()
    author_tags = soup.select('.author')

    for author in author_tags:
        authors.add(author.string)

    return authors

def get_all_quotes(page_number=1):
    quotes = []
    soup = get_quote_page(page_number)
    all_quote_tags = soup.select('.text')

    for quote in all_quote_tags:
        quotes.append(quote.string)

    return quotes


def get_top_ten_tags(page_number=1):
    tags = []
    soup = get_quote_page(page_number)
    tag_box = soup.select('.col-md-4.tags-box')
    all_tags = tag_box[0].select('.tag')

    for tag in all_tags:
        tags.append(tag.text)

    return tags


# print(get_all_authors())
# print(get_all_quotes())
# print(get_top_ten_tags())

def get_authors_on_all_pages():
    page = 1
    unique_authors = set()

    while True:
        print(f'-------- Page {page} Scraping --------')
        soup = get_quote_page(page)

        unique_authors = unique_authors.union(get_authors_from_soup(soup))
        print(unique_authors)

        next_page = soup.select('.col-md-8')[1].select('.next')
        print(f'\nlength of next page: {len(next_page)}\n')
        if next_page:
            page += 1
        else:
            break
    
    return unique_authors


get_authors_on_all_pages()
