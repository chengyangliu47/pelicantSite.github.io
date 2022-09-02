from cmath import log
import pandas
import json

def test():   
  
    # Opening JSON file
    f = open('./jsonData.json')
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list
    for i in data:
        print(i)
    
    # Closing file
    f.close()

test()
