#Python Challenge Task One
#flp
#Task: find each letter in the alphabet and increment it by two to find the sentence
alpahbet = "abcdefghijklmnopqrstuvwxyz" * 2

sentence = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

url = "http://www.pythonchallenge.com/pc/def/map.html"

def translate(word):
	output = ""
	for x in range(1,len(word)):
		letter = word[x]
		if letter.isalpha():
			translatedLetter = alpahbet[alpahbet.find(letter)+2]
			output += translatedLetter
		else:
			output += letter
	return(output)

print (translate(sentence))
print (translate(url))