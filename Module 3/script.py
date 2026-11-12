a_list=list([3,4,6,5,3])
xyz=[24.234,2,3,4,134]

my_set={134,2,3}
if isinstance(my_set,set):
    print('This is a set')

other_set=set(xyz)

union_result=other_set.union(my_set)
union_result_2=my_set | other_set # | means union
print(f"Union function: {union_result_2 | union_result}")

intersect_result = other_set.intersection(my_set)
intersect_result_sign = other_set & my_set # & means intersect
print(f"Intersect function: {intersect_result_sign}")

set_difference=union_result.difference(my_set)
print(f"Difference between {union_result} and {my_set} is: {set_difference}")
sign_difference=union_result - my_set
print(sign_difference==set_difference)


list1=['red','green','blue','black']
list2=['orange','black','white','yellow']

set1=set(list1)
set2=set(list2)
unique_set = set1 | set2
print(unique_set)

#CONDITIONALS

age=18

if age>=18:             #if completed first, conditional ends
    print("Over 18")
elif age==18:
    print("Equals 18")
else:
    print("Minor")


color='red'
in_city=True
if color!='green' and in_city:
    print("Don't move")
elif color!= 'green' or in_city is False or 3>5 or 1!=1:
    print("You are free to drive")

#and, or, not in, in

studenti=['Rigoni']
students=['Rini','Edlira','Ernesi','Drini','Syari','Olti']

if studenti not in students:
    students.append(studenti)
else:
    print(students)

# % - module
# ** - exponent

print(6%2)