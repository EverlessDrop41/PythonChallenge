#Python Challenge 2
#Find the less than average characters

def solve(string):
	average = 0
	timesLetterFound = {}
	for let in string:
		if let in timesLetterFound:
			timesLetterFound[let] += 1
		else:
			timesLetterFound[let] = 1
	total = 0
	for key in timesLetterFound:
		total += timesLetterFound[key]

	average = int(total / len(timesLetterFound))
	word = ""
	for key in timesLetterFound:
		if timesLetterFound[key] < average:
			print ("{},{}".format(key,timesLetterFound[key]))
			word += key
	print (word)

text = open("pychall-2-text.txt").read()

solve(text)