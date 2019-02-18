import re
fileContent=open("ActualData.txt")
content=fileContent.read()

print sum([ re.findall('[0-9]+',content) ])

digitList=list()


for line in fileContent:
	digits=re.findall('[0-9]+',line)
	if len(digits) > 0:
			digitList.append(digits)
sum=0			
for digit in digitList:
	if len(digit) >= 1:
		for ind in digit:
			sum+=int(ind)
	
print(sum)