import json
filename = 'numbers.json'
f=open(filename,"r")
data=json.loads(f.read())
print(data)
f.close()