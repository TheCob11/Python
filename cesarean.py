import string
def encrypter(shift, msg):
	shift = int(shift)
	msgChars = list(msg)
	for x in range(len(msgChars)):
		if msgChars[x] in string.ascii_letters:
			if chr(ord(msgChars[x])+shift) not in string.ascii_letters:
				if msgChars[x] in string.ascii_lowercase:
					lowerOLap = (ord(msgChars[x])+shift)-ord("z")
				elif msgChars[x] in string.ascii_uppercase:
					upperOLap = (ord(msgChars[x])+shift)-ord("Z")
					msgChars[x] = chr(ord("A")+(upperOLap-1))				
			elif msgChars[x] in string.ascii_uppercase and chr(ord(msgChars[x])+shift) in string.ascii_lowercase:
					upperOLap = (ord(msgChars[x])+shift)-ord("Z")
					msgChars[x] = chr(ord("A")+(upperOLap-1))
			else:
				msgChars[x] = chr(ord(msgChars[x])+shift)		
	msgShifted = ''.join(msgChars)
	return msgShifted
while True:
	shiftInput = input("Shift? ")
	try:
		int(shiftInput)
	except:
		print("Not an int")
	else:
		break
msgInput = input("Message? ")
print(encrypter(shiftInput, msgInput))	
