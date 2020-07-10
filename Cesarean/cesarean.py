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

def CesAIrean(mAIsg):
	mAIsgWords = str.split(mAIsg)
	mAIsgLength = len(mAIsgWords)
	mAIsgRoyale = ["","","","","","","","","","","","","","","","","","","","","","","","","","",""]
	for x in range(26+1):
		mAIsgYups = 0
		mAIsgChecks = []
		mAIsgResult = []
		for w in range(len(mAIsgWords)):
			wordCheAIcker = Cesarean(x, mAIsgWords[w])
			if wordCheck(wordCheAIcker) == True:
				mAIsgYups = mAIsgYups + 1
				mAIsgChecks.append(True)
				mAIsgResult.append(wordCheAIcker)
			else:
				mAIsgChecks.append(False)
		mAIsgRoyale[x] = mAIsgYups
		if all(mAIsgChecks) == True:
			return("".join(mAIsgResult))
	return(Cesarean((mAIsgRoyale.index(max(mAIsgRoyale))), mAIsg))
#ecOrDc = input("encrypt or Decrypt(1 for encrypter, 2 for decrypter)? ")
#while True:
#	try:
#		int(ecOrDc)
#	except:
#		print("Not an int")
#	else:
#		break
#
#fileOpen = input("Use the file?(Y/N) ")
#while True:
#	if fileOpen == "y" or fileOpen == "Y":
#		file = open("file.txt", "rt")
#		break
#	elif fileOpen == "n" or fileOpen == "N":
#		break
#	else:
#		print("Y or N")
#
#while True:
#	if int(ecOrDc) == 1:
#		while True:
#			shiftInput = input("Shift? ")
#			try:
#				int(shiftInput)
#			except:
#				print("Not an int")
#			else:
#				break
#		if fileOpen == "y" or fileOpen == "Y":
#			print(Cesarean(shiftInput, file.read()))	
#		else:
#			msgInput = input("Message? ")
#			print(Cesarean(shiftInput, msgInput))	
#			break
#	elif int(ecOrDc) == 2:
#		if fileOpen == "y" or fileOpen == "Y":
#			CesAIrean(file.read())
#		elif fileOpen == "n" or fileOpen == "N":
#			mAIsgInput = input("Message? ")
#			print(CesAIrean(mAIsgInput))
#	else:
#		print("Input 1 or 2")
#	break



with open("file.txt", "rt") as f:
	for line in f:
		line = line.split("\n")
		print(CesAIrean(line[0]))
