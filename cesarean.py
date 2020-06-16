import string
def encrypter(shift, msg):
	msgChars = list(msg)
	for x in range(len(msgChars)):
		if msgChars[x] in string.ascii_letters:
			if chr(ord(msgChars[x])+shift) not in string.ascii_letters:
				if msgChars[x] in string.ascii_lowercase:
					lowerOLap = (ord(msgChars[x])+shift)-ord("z")
			elif msgChars[x] in string.ascii_uppercase:
					upperOLap = (ord(msgChars[x])+shift)-ord("Z")
					msgChars[x] = chr(ord("A")+(upperOLap-1))
			else:
				msgChars[x] = chr(ord(msgChars[x])+shift)		
	msgShifted = ''.join(msgChars)
	return(msgShifted)
shiftInput = input("Shift? ")
msgInput = input("Message? ")
encrypter(shiftInput, msgInput)