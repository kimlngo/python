import pypdf

f = open('Working_Business_Proposal.pdf', 'rb') #rb: read binary
pdf_reader = pypdf.PdfReader(f)
print(pdf_reader.get_num_pages())

page_one = pdf_reader.get_page(0)
page_one_text = page_one.extract_text()
print(page_one_text)

# f.close()

# pdf writer
# pdf_writer = pypdf.PdfWriter()
# pdf_writer.add_page(page_one)

# pdf_output = open('Extracted-Pdf.pdf', 'wb')
# pdf_writer.write(pdf_output)

# read all content of pdf

pdf_by_page = []

for page_num in range(pdf_reader.get_num_pages()):
    page = pdf_reader.get_page(page_num)
    pdf_by_page.append(page.extract_text())

print('============================================')
print(pdf_by_page)

f.close()
# pdf_output.close()