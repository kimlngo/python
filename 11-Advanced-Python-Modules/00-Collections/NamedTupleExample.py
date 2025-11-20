from collections import namedtuple

Student = namedtuple('Student', ['firstName', 'lastName', 'age', 'major'])
kimlngo = Student(firstName='Thomas', lastName='Ngo', age=37, major=['Computer Engineering', 'Electronics', 'Physics'])

antran = Student(firstName='An', lastName='Tran', age=28, major=['cooking', 'nailing'])
print(kimlngo) #Student(firstName='Thomas', lastName='Ngo', age=37, major=['Computer Engineering', 'Electronics', 'Physics'])

print(kimlngo.firstName) #Thomas
print(kimlngo[0]) #Thomas

print(antran) #Student(firstName='An', lastName='Tran', age=28, major=['cooking', 'nailing'])
print(antran.major) #['cooking', 'nailing']
print(antran[3]) #['cooking', 'nailing']