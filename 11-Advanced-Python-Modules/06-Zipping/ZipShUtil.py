import shutil

dir_to_zip = "D:\\github\Python\\11-Advanced-Python-Modules\\06-Zipping\\extracted_content"
output_file_name = "example"

#zip
# shutil.make_archive(output_file_name, 'zip', dir_to_zip)

#unzip
shutil.unpack_archive("example.zip", "final_extraction", "zip")