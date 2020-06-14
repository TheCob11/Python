import string
def encrypter(shift, msg):
	msgChars = list(msg)
	for x in range(len(msgChars)):
		if msgChars[x] in string.ascii_letters:
			msgChars[x] = chr(ord(msgChars[x])+shift)
	msgShifted = ''.join(msgChars)
	return(msgShifted)
encrypter(1, 'Online Ganondorfs at 200% are stupid.')