import requests
key = "2d330926-ee50-41fb-9bfa-4b161269bfa3"
r = requests.get('https://www.dictionaryapi.com/api/v3/references/collegiate/json/voluminous?key='+key)
print(r.text)
import string
def encrypter(shift, msg):
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





#Gotato- ["got at","got to","got it","potato","agitato","rotator","gotta","got into","potatoes","rotators","rotatory","annotator","got about","got after","got along","got it on","rotatores","annotators","got across","got around"]
#Voluminous- [{"meta":{"id":"voluminous","uuid":"0d01b967-971f-4ec5-8fe0-10513d29c39b","sort":"220130400","src":"collegiate","section":"alpha","stems":["voluminous","voluminously","voluminousness","voluminousnesses"],"offensive":false},"hwi":{"hw":"vo*lu*mi*nous","prs":[{"mw":"v\u0259-\u02c8l\u00fc-m\u0259-n\u0259s","sound":{"audio":"volumi02","ref":"c","stat":"1"}}]},"fl":"adjective","def":[{"sseq":[[["sense",{"sn":"1 a","dt":[["text","{bc}having or marked by great {a_link|volume} or bulk {bc}{sx|large||} "],["vis",[{"t":"long {wi}voluminous{\/wi} tresses"}]]],"sdsense":{"sd":"also","dt":[["text","{bc}{sx|full||} "],["vis",[{"t":"a {wi}voluminous{\/wi} skirt"}]]]}}],["sense",{"sn":"b","dt":[["text","{bc}{sx|numerous||} "],["vis",[{"t":"trying to keep track of {wi}voluminous{\/wi} slips of paper"}]]]}]],[["sense",{"sn":"2 a","dt":[["text","{bc}filling or capable of filling a large volume or several {a_link|volumes} "],["vis",[{"t":"a {wi}voluminous{\/wi} literature on the subject"}]]]}],["sense",{"sn":"b","dt":[["text","{bc}writing or speaking much or at great length "],["vis",[{"t":"a {wi}voluminous{\/wi} correspondent"}]]]}]],[["sense",{"sn":"3","dt":[["text","{bc}consisting of many folds, coils, or convolutions {bc}{sx|winding|winding:2|}"]]}]]]}],"uros":[{"ure":"vo*lu*mi*nous*ly","fl":"adverb"},{"ure":"vo*lu*mi*nous*ness","fl":"noun"}],"et":[["text","Late Latin {it}voluminosus{\/it}, from Latin {it}volumin-, volumen{\/it}"]],"date":"1611{ds||3||}","shortdef":["having or marked by great volume or bulk : large; also : full","numerous","filling or capable of filling a large volume or several volumes"]}]