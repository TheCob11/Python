import json
import requests
import string
key = "2d330926-ee50-41fb-9bfa-4b161269bfa3"
def wordCheck(word):
	wordResult = requests.get('https://www.dictionaryapi.com/api/v3/references/collegiate/json/'+word+'?key='+key)
	outputJson = wordResult.json()
	if len(outputJson) == 0:
		return(False)
	if type(outputJson[0]) is not str:
		return(True)
	else:
		return(False)
def Cesarean(shift, msg):
	shift = int(shift)
	shift = shift%26
	msgChars = list(msg)
	for x in range(len(msgChars)):
		if msgChars[x] in string.ascii_letters:
			if chr(ord(msgChars[x])+shift) not in string.ascii_letters:
					if msgChars[x] in string.ascii_lowercase:
						lowerOLap = (ord(msgChars[x])+shift)-ord("z")
						msgChars[x] = chr(ord("a")+(lowerOLap-1))
					elif msgChars[x] in string.ascii_uppercase:
						upperOLap = (ord(msgChars[x])+shift)-ord("Z")
						msgChars[x] = chr(ord("A")+(upperOLap-1))
			elif msgChars[x] in string.ascii_uppercase and chr(ord(msgChars[x])+shift) not in string.ascii_uppercase:
				upperOLap = (ord(msgChars[x])+shift)-ord("Z")
				msgChars[x] = chr(ord("A")+(upperOLap-1))
			else:
				msgChars[x] = chr(ord(msgChars[x])+shift)		
	msgShifted = ''.join(msgChars)
	return msgShifted
#while True:
#	shiftInput = input("Shift(enter negative shift to decrypt)? ")
#	try:
#		int(shiftInput)
#	except:
#		print("Not an int")
#	else:
#		break
#msgInput = input("Message? ")
#print(Cesarean(69, "It's gonna take a lot to take me away from you"))	
def CesAIrean(mAIsg):
	mAIsgWords = str.split(mAIsg)
	for x in range(26):
		mAIsgChecks = []
		mAIsgResult = []
		for w in range(len(mAIsgWords)):
			wordCheAIcker = Cesarean(x, mAIsgWords[w])
			if wordCheck(wordCheAIcker) == True:
				mAIsgChecks.append(True)
				mAIsgResult.append(wordCheAIcker)
			else:
				mAIsgChecks.append(False)
		if all(mAIsgChecks) == True:
			return("The message was '"+' '.join(mAIsgResult)+"'")

mAIsgInput = input("What message?")
print(CesAIrean(mAIsgInput))