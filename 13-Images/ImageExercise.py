from PIL import Image

mac = Image.open('example.jpg')
# mac.show()
print(type(mac)) #<class 'PIL.JpegImagePlugin.JpegImageFile'>
print(mac.size)  #(1993, 1257)
print(mac.filename) #example.jpg
print(mac.format_description) #JPEG (ISO 10918)

#image crop
pencil = Image.open('pencils.jpg')
print(pencil.size) #(1950, 1300)

# top 3 pencils
x = 0
y = 0
w = 1950 / 3
h = 1300 / 10
# pencil.crop((x,y,w,h)).show()

# bottom 3 penciles
x = 0
y = 1100

w = 1950 / 3
h = 1300
# pencil.crop((x,y,w,h)).show()

#crop the computer
halfway = mac.size[0]/2 # 1993/2
x = halfway - 200
w = halfway + 200

y = 800
h = mac.size[1] #1257
mac.crop((x,y,w,h))

#resize
# mac.resize((3000, 500)).show()

#rotate
# mac.rotate(90).show()

#Transparency
blue = Image.open('blue.jpg')
blue.putalpha(128) #half-transparent
# blue.show()

red = Image.open('red_color.jpg')
red.putalpha(128)
# red.show()

#pasting one on top of another
blue.paste(im=red, box=(0,0), mask=red)
blue.show()

#save image
blue.save('purple-save.png')
purple_save = Image.open('purple-save.png')
purple_save.show()