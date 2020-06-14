import string
def encrypter():
	while True:
		shift = input("Shift? ")
		try:
			int(shift)
		except:
			print("Not an integer")
		else:
			shift=int(shift)
			break
	msg = input("Message? ")
	msgChars = list(msg)
	for x in range(len(msgChars)):
		if msgChars[x] in string.ascii_letters:
			msgChars[x] = chr(ord(msgChars[x])+shift)
	msgShifted = ''.join(msgChars)
	print(msgShifted)
encrypter()
def encrypterAlphabet():
	while True:
		shift = input("Shift? ")
		try:
			int(shift)
		except:
			print("Not an integer")
		else:
			shift=int(shift)
			break
	msg = input("Message? ")
	msgChars = list(msg)
	for x in range(len(msgChars)):
		if (ord(msgChars[x]) >= ord('a') and ord(msgChars[x])<=ord('z') ) or (ord(msgChars[x])<=ord('Z') and ord(msgChars[x])>=ord('A')): 
			msgChars[x] = chr(ord(msgChars[x])+shift)
	msgShifted = ''.join(msgChars)
	print(msgShifted)
encrypterAlphabet()
