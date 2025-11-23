import os
import re

start_dir = "D:\\github\\Python\\11-Advanced-Python-Modules\\Puzzle\\instruction\\extracted_content"
phone_pattern = r'(\d{3})-(\d{3})-(\d{4})'
compile_ptn= re.compile(phone_pattern)

def browse_and_extract_phones(start_dir):
    for root, _, files in os.walk(start_dir):
        for file in files:
            file_name = root + "\\" + file
            f = open(file_name, 'r')
            phones = extract_phone_number(f.read())
            if len(phones) != 0:
                print(f'filename: {file}')
                print(f'--> {phones}')

def extract_phone_number(str):
    search_result = re.search(compile_ptn, str)

    if search_result == None:
        return ""
    else:
        return search_result.group()
    
browse_and_extract_phones(start_dir)