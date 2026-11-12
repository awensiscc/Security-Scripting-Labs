
import json

with open("employees.json") as emp:
    # load the file in json format
    data = json.load(emp)

    # use a for loop to iterate over each array element
    for i in range(len(data['employees'])):

        # print the first 4 elements in the array
        print ("Name:", data['employees'][i]['Name'])
        print ("DOB:", data['employees'][i]['DOB'])
        print ("id:", data['employees'][i]['id'])
        print ("Email:", data['employees'][i]['Email'])
        print ("Duties:")

        # print the duties array
        for duty in data['employees'][i]['Duties']:
            print (duty)

        # print the address
        print ('Address:')
        for key, value in dict.items(data['employees'][i]['Address']):
            print (value)

        # print blank line
        print ('\n')

