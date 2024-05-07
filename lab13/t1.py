import csv #import csv
import json #import json
import random #import random
import string #import string

""" this is a comment
By Mark Shaposhnik (marguuss)
If this concerns you, here is the file structure in the first iteration.

CSV
airport         state           index           country
3 char          2 char          5 dec num       2 char

JSON
airport     3 char
state       2 char
index       5 dec num
country     2 char

P.S. All data is random

the end of the comment"""

class AirportDataGenerator: # class declaration
    def __init__(self): # constructor declaration
        self.runner() # method execution

    def runner(self): # method for a short runlist
        self.start_csv() # execution of method called "start_csv"
        self.convert_to_json() # execution of method called "convert_to_json"
        self.student2() # execution of method called "student2"
        self.student3() # execution of method called "student3"
        self.student4() # execution of method called "student4"
        self.student5() # execution of method called "student5"

    def start_csv(self): #first method here
        filename = 'random.csv' # file name here
        data = [] # empty array declaration
        for _ in range(10000): # for loop declaration
            airport = ''.join(random.choices(string.ascii_uppercase, k=3)) # creation of a random string
            state = ''.join(random.choices(string.ascii_uppercase, k=2)) #creation of a random string
            index = ''.join(random.choices(string.digits, k=5)) # creation of a random number
            country = ''.join(random.choices(string.ascii_uppercase, k=2)) # creation of a random string
            data.append([airport, state, index, country]) #addintion to the array
        
        try: # its just try, you know what it is 
            with open(filename, 'w', newline='', encoding='utf-8') as file: # opening file
                writer = csv.writer(file) # file creation
                writer.writerow(["Airport", "State", "Index", "Country"]) # first line declaration
                writer.writerows(data) # saveing data
            print(f"Data successfully written to file {filename}.") # print conformation
        except Exception as e: # exception, you know...
            print(f"An error occurred while writing to the file: {e}") #error print here

    def convert_to_json(self): # conversion method, turn csv to json
        csv_filename = 'random.csv' # filename for csv
        json_filename = 'random.json' # anotherfilename, json one
        try: # try, again, you know it
            with open(csv_filename, mode='r', encoding='utf-8') as file: # opening file 
                reader = csv.DictReader(file) # reading file
                data = list(reader) # getting the data from file name
            
            with open(json_filename, 'w', encoding='utf-8') as file: # opening file as well
                json.dump(data, file, indent=4) # overwriting to json
            print(f"Data successfully written to file {json_filename}.") # conformation print
        except Exception as e: #I think you get it
            print(f"An error occurred while writing to the file: {e}") # error print
            #And yes, some of your student know english well enough, you know...

    def student2(self):
        # No code yet
        pass

    def student3(self):
        # No code yet
        pass

    def student4(self):
        # No code yet
        pass

    def student5(self):
        # No code yet
        pass

generator = AirportDataGenerator() # class execution here