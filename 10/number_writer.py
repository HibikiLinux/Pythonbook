
import json

numbers = [2, 3, 5, 7, 11, 13]
f=open("numbers.json","w")
f.write(json.dumps(numbers))
#json.dump(numbers,f)
f.close()