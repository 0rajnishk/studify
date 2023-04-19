import os
import PyPDF2

# Open the PDF file
pdf_file = open('drive/diploma/endterm/diploma.pdf', 'rb')
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Define the titles
titles = ['Sem1 Eng1', 'Sem1 Maths1', 'Sem2 Eng2',
          'Sem2 Intro to Python', 'Sem2 Maths2', 'BDM', 'Business Analytics']


# Define the output folder
output_folder = 'drive/diploma/endterm/output'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Loop through the titles and extract the pages between them
for i in range(len(titles) - 1):
    start_title = titles[i]
    end_title = titles[i + 1]
    start_page = None
    end_page = None

    # Find the page numbers of the start and end titles
    for page_num, page in enumerate(pdf_reader.pages):
        text = page.extract_text().strip()

        if start_title in text:
            start_page = page_num
        elif end_title in text:
            end_page = page_num
            break

    # Extract the pages and save them with the name of the start title
    if start_page is not None and end_page is not None:
        output_file_name = os.path.join(output_folder, start_title + '.pdf')
        pdf_writer = PyPDF2.PdfWriter()
        for page_num in range(start_page, end_page):
            pdf_writer.add_page(pdf_reader.pages[page_num])
        with open(output_file_name, 'wb') as output_file:
            pdf_writer.write(output_file)

# Extract the pages from the last title to the end of the PDF and save them with the name of the last title
last_title = titles[-1]
last_page = None
for page_num, page in enumerate(pdf_reader.pages):
    text = page.extract_text().strip()
    if last_title in text:
        last_page = page_num
if last_page is not None:
    output_file_name = os.path.join(output_folder, last_title + '.pdf')
    pdf_writer = PyPDF2.PdfWriter()
    for page_num in range(last_page, len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])
    with open(output_file_name, 'wb') as output_file:
        pdf_writer.write(output_file)

# Close the PDF file
pdf_file.close()
