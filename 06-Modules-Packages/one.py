
def my_func():
    print("This is my_func in one.py")

print("ONE.PY TOP LEVEL")

if __name__ == '__main__':
    print("ONE.PY is being run directly")
else:
    print(f'__name__ = {__name__}')
    print("ONE.PY has been imported")

# $ python one.py 
# ONE.PY TOP LEVEL
# ONE.PY is being run directly