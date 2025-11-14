class Student():
    
    #CLASS OBJECT ATTRIBUTE
    #SAME FOR ANY INSTANCE OF A CLASS
    goals = 'Study and Graduate'

    # constructor
    def __init__(self, name, grade, favorite_sports):
        #Attributes
        #Take in argument & assign it using self.attribute_name
        self.name = name
        self.grade = grade
        self.favorite_sports = favorite_sports

    # Operation/Actions --> methods
    def study(self):
        print('I am studying!!!')
        
    def to_string(self):
        return 'Student info: name: {}, grade: {}, favorite sports: {}, goals: {}'.format(self.name, self.grade, self.favorite_sports, self.goals)
    
    def add_favorite_sport(self, new_sport):
        self.favorite_sports.append(new_sport)
    

#create instance of Sample
student = Student('James', 8, ['soccer', 'badminton'])
print(f'Student goals: {student.goals}') #Student goals: Study and Graduate
print(f'Student name: {student.name}')   #Student name: James
print(f'Student grade: {student.grade}') #Student grade: 8
print(f'Student favorite sports: {student.favorite_sports}') #Student favorite sports: ['soccer', 'badminton']

student.study()
print(student.to_string()) #Student info: name: James, grade: 8, favorite sports: ['soccer', 'badminton'], goals: Study and Graduate

student.add_favorite_sport('volleyball')
print(f'Student favorite sports: {student.favorite_sports}') #Student favorite sports: ['soccer', 'badminton', 'volleyball']


print(type(student)) #<class '__main__.Student'>