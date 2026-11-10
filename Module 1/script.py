temperature=45 #variables
name='Drin'
unit='F'

#Data Structures
students=['student1','Student2','student3',6,0.676]

t1=(3,3,5,7,4) #immutable
s1={3,3,5,7,4,3,3,3,4} #unique only
d1={'Edlira':17,'Rini':17,'Lirak':23} #key-value pairs
print(d1['Rini'])
print(type(d1['Edlira']))
print("------"*5)

students.append(True)
for student in students:
    print(student)
print(students.index('student3')) #Case sensitive
students.sort() #Sorts; must have same data type
print(students)
for key,value in d1.items():
    print(f"{key} - {value}")