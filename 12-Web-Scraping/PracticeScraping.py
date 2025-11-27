import requests
import bs4

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

def get_url(page_num):
    return BASE_URL.format(page_num)

def extract_title_in_one_page(page_num):
    titles = []
    books_on_page = requests.get(get_url(page_num))
    soup = bs4.BeautifulSoup(books_on_page.text, 'lxml')

    product_pods = soup.select('.product_pod')
    # print(type(product_pods))
    # print(len(product_pods))
    # print(type(product_pods[0]))

    #extract the class star-rating Two
    for prod in product_pods:
        if prod.select('.star-rating.Two'): #for class with space in between, change space to dot (.)
            titles.append(prod.select('a')[1]['title'])

    return titles

def scrape_titles_with_two_stars():
    all_titles = []
    for page in range(1,6):
        one_page_titles = extract_title_in_one_page(page)
        
        if one_page_titles:
            all_titles.extend(one_page_titles)

    
    print(all_titles)

scrape_titles_with_two_stars()
