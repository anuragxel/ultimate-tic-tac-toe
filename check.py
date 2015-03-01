import json

f = open("foo.csv")
dick = json.load(f)
print len(dick)
