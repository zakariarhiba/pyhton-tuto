# json houya langage apis , n9dro n5dmo bih me3a python object
import json

#hada json
user_json = '{ "first_name" : "zakaria","second_name" : "RHIBA", "age" : 18 }'

#kifach nrodoh objet
user = json.loads(user_json)

print(user)

# kifach nrodo objet l json 
car = {'name':'mersidice','speed':'120KM/h'}

car_json = json.dumps(car)
print(car)
    