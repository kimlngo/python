import requests
import bs4

result = requests.get("https://www.example.com/")
print(type(result))

soup = bs4.BeautifulSoup(result.text, 'lxml')
print(soup.select('title')) #[<title>Example Domain</title>]
print(soup.select('p')) #[<title>Example Domain</title>]
# [<p>This domain is for use in documentation examples without needing permission. Avoid use in operations.</p>, <p><a href="https://iana.org/domains/example">Learn more</a></p>]
print(soup.select('h1')) #[<h1>Example Domain</h1>]

#get text without tags
print(soup.select('title')[0].getText()) #Example Domain