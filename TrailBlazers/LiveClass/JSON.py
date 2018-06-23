import json

student_scores = {'Tom':[20,30],
                  'Rob':[10,20],
                  'Tob':[10,20]}
                  
#How about writing the dictionary to the file
#fp = open("/data/mydatafile.txt","w")
##TypeError: must be str, not dict
#fp.write(student_scores)
#fp.close()


serialized_data = json.dumps(student_scores)

#print(serialized_data)                 


fp = open("data/mydatafile.txt","w")
fp.write(serialized_data)
fp.close()

fp = open("data/mydatafile.txt","r")
for line in fp:
    print(line)

#print("Tob scored" , line['Tob'][0])
    
retrieved_ds = json.loads(line)

print("Tob scored" , retrieved_ds['Tob'][0])



