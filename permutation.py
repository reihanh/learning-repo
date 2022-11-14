
def permute(string, pocket=""):
	if len(string) == 0:
		print(pocket)
	else:
		# make 3 variable, each letter, front string, back string
		for i in range(len(string)):
			letter = string[i]
			front = string[0:i]
			back = string[i+1:]
			together = front + back
			permute(together, letter + pocket)


print(permute("AB",""))


# note
"""
string slicing
string[start:end:jump]

string[0:0] =>> ""

"""