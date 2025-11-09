print('========================================')
print('LEVEL 1 PROBLEMS')
print('OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name')
print("old_macdonald('macdonald') --> MacDonald")

def old_macdonald(name):
    output = ''
    for idx, letter in enumerate(name):
        if idx in [0,3]:
            output += letter.upper()
        else:
            output += letter
    
    return output

print(old_macdonald('macdonald'))
print(old_macdonald('mac'))

print('========================================')
print('MASTER YODA: Given a sentence, return a sentence with the words reversed')
""" 
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'
 """

def master_yoda(text):
    reverse_txt = text.split()[::-1]
    return ' '.join(reverse_txt)

print(master_yoda('I am home'))
print(master_yoda('We are ready'))

print('========================================')
print('ALMOST THERE: Given an integer n, return True if n is within 10 of either 100 or 200')

def almost_there(n):
    return abs(n - 100) <= 10 or abs(n - 200) <= 10

print(almost_there(90)) #True
print(almost_there(104)) #True
print(almost_there(150)) #False
print(almost_there(209)) #True