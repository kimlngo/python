import csv
import pypdf
import re

phone_search_ptn = re.compile(r'\d{3}.\d{3}.\d{4}')

def grab_google_drive_link():
    link_file = open('find_the_link.csv', encoding='utf-8')

    csv_data = csv.reader(link_file)

    data_lines = list(csv_data)
    num_of_lines = len(data_lines)

    link = ''
    index = 0

    while index < num_of_lines:
        link += data_lines[index][index]
        index += 1

    print(link)

def search_phone_number():
    f = open('Find_the_Phone_Number.pdf', 'rb')
    pdf_reader = pypdf.PdfReader(f)
    total_page = pdf_reader.get_num_pages()

    for page_num in range(total_page):
        page = pdf_reader.get_page(page_num)
        text = page.extract_text()

        phone = re.search(phone_search_ptn, text)
        if phone: 
            print("--------------")
            print(f'found phone: {phone.group()}')


search_phone_number()