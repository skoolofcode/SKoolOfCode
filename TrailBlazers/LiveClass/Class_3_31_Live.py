#Understanding Git : This is a modification to the file.
#Let's store dictionary into a file
student_scores = {'Rob':[10,20,30],
                  'Tommy':[34,45],
                  'Ram' : [50,50,10]}
print("This is my dictionary",student_scores)

#fp = open("/data/file_3_31.txt","w")
#fp.write(student_scores)
#fp.close()
#The code above will give an erro - "TypeError: must be str, not dict"

import json

print("Tom's score ", student_scores['Tommy'])

dict_to_string = json.dumps(student_scores)
fp = open("data/ABC.txt","w")
fp.write(dict_to_string)
fp.close()

#Retrieve this back from a file and store as a dictonary

fp = open("data/ABC.txt","r")
line = fp.readline()
fp.close()

print("Retrieve line is ", line)
print("Type of line variable", type(line))
#print("Tom's score ", line['Tommy'])

retrieve_as_dictionary = json.loads(line)
print("Type of  retrieve_as_dictionary", type(retrieve_as_dictionary))
print("Tom's score ", retrieve_as_dictionary['Tommy'])








