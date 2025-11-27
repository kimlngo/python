from PIL import Image

word_matrix = Image.open('word_matrix.png')
print(word_matrix.size)

mask = Image.open('mask.png')
print(mask.size)

mask_double = mask.resize(word_matrix.size)
mask_double.putalpha(150)
word_matrix.paste(im=mask_double, box=(0,0), mask=mask_double)
word_matrix.show()

word_matrix.save('word_matrix_result.png')