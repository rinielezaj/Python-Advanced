from typing import Dict,List


pcs:Dict[int,'str'|List[str]]={3:'Lenovo',
                               4:'HP',
                               5:['msi','Dell']
                               }
print(pcs[5][1]) #kur dihet indeksi
for key,value in pcs.items():  #kur nuk dihet indeksi
    if isinstance(value,list): #kontrollon llojin
        for brand in value:
            print(f"Per pc nr.{key}, eshte brendi: {brand}")
    else:
        print(f"Per pc nr.{key}, eshte brendi: {value}")

example='PythonListMethodsExplained'
example=example.lower()
count:[str,int]={}
for char in example:
    if char not in count.keys():
        count[char]=1
    else:
        count[char]+=1
print(count)
print(pcs.items())

#Variablet munden me qene edhe shqip


qytetet:List[str|int]=['Prishtina','New York',5,'Prizreni','Tirana','Shkupi']
print(len(qytetet))
print(qytetet.index('Prizreni'))
qytetet.append('Londra')
for i in range(5):
    qytetet.append(f"Elementi nr.{i}") #shton elementin ne fund te listes
print(qytetet.count('Elementi nr.33')) #sa here eshte elementi ne liste
qytetet.insert(0,5)
print(qytetet)

#TUPLES AND SETS

words=('spam','sausages','eggs','sausages')
print(words.index('sausages'))
print(words.count('spam'))

x={3,7,6,"3",False,False,True} #Set sorts from smallest to largest and is unique only
print(x)
print(len(x))


student={1:{"emri":"Lirak","mosha":23,"student":False},
         2:{"emri":"Rini","mosha":18,"student":True}}

for key,val in student.items():
    for k,v in val.items():
        print(f"Studenti me id: {key}, {k}:{v}")





















