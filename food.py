#coding=utf-8
import random
InputDataName = "restaurant"

inputdata = open(InputDataName,"r")
result = []

for line in inputdata:
	line = line.strip("\n")
	if not len(line):
		continue
	#print line
	result.append(line)
#print result

inputdata.close()

num = random.randint(1, len(result))
print result[num-1]
