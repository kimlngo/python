import os
import shutil

f = open("D://github//Python//11-Advanced-Python-Modules//01-Files-Folders//practice.txt", 'w+')
f.write('Test String 1')
f.close()

print(os.getcwd())
print(os.listdir())
print(os.listdir("D:\github\Python"))
print(os.listdir("D://github//Python"))

#move file/folder
shutil.move('D://github//Python//11-Advanced-Python-Modules//01-Files-Folders//practice.txt', "D://github//Python//11-Advanced-Python-Modules//01-Files-Folders//tmp")