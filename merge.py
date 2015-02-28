import json

old = open("old.csv")
other = open("new.csv")
old_dic = json.load(old)
other_dic = json.load(other)
old.close()
other.close()
yay = {}
for key,value in old_dic.iteritems():
    if key not in yay:
        yay[key] = value

for key,value in other_dic.iteritems():
    if key not in yay:
        yay[key] = value

yay_file = open("yay.json","w")
json.dump(yay,yay_file)
print len(yay)
