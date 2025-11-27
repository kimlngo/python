import requests
import bs4

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0 Safari/537.36"
}

# response = requests.get("https://en.wikipedia.org/wiki/Ben_Affleck", headers=headers)
# soup = bs4.BeautifulSoup(response.text, "lxml")

# for item in soup.select('.vector-toc-text'):
#     print(item.text)

# .mw-file-element
image_get = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)", headers=headers)
soup = bs4.BeautifulSoup(image_get.text, "lxml")

computer = soup.select('.mw-file-element')[1]
print(type(computer))
print(computer['src'])
image_link = 'https:' + computer['src']
image = requests.get(image_link, headers=headers)

#save an image
f = open('computer-image.jpg', 'wb') #wb: write binary
f.write(image.content)
f.close()