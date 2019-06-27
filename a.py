userinput = input()
count ={"UPPER":0,"LOWER":0}
for i in userinput:
	if userinput.isupper():
		count["UPPER"]+=1
	elif userinput.islower():
		count["LOWER"]+=1
	else:
		pass
	print("Upper case letter",count["UPPER"])
	print("LOWER case letter",count["LOWER"])

