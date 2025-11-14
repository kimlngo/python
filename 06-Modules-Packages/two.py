import one

one.my_func()
print("TWO.PY TOP LEVEL")

if __name__ == '__main__':
    print("TWO.PY is being run directly")
else:
    print("TWO.PY has been imported")

# $ python two.py 
# ONE.PY TOP LEVEL
# __name__ = one
# ONE.PY has been imported
# This is my_func in one.py
# TWO.PY TOP LEVEL
# TWO.PY is being run directly