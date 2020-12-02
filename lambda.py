person = [{'name': 'Harry','house': 'Gryffindor'},{'name':'Cho', 'house': 'Ravenclaw'}, {'name': 'Dreco','house': 'Slytherin'}]



person.sort(key= lambda person: person['name'])



print(person)