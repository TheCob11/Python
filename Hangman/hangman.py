import string
def hangman(word):
	word = word.lower()
	word = list(word)
	wordKnown = []
	for l in word:
		if l not in string.ascii_letters:
			word.remove(l)
		wordKnown.append("_ ")
	hits = 0
	while hits<7:
		if hits == 0:
			print('''
------|
|     |
|     |
|
|
|
|
|
|
^''')	
		elif hits == 1:
			print('''
------|
|     |
|     |
|     0
|
|
|
|
|
^''')
		elif hits == 2:
			print('''
------|
|     |
|     |
|     0
|     |
|
|
|
|
^''')
		elif hits == 3:
			print('''
------|
|     |
|     |
|     0
|    /|
|
|
|
|
^''')
		elif hits == 4:
			print('''
------|
|     |
|     |
|     0
|    /|\\
|
|
|
|
^''')		
		elif hits == 5:
			print('''
------|
|     |
|     |
|     0
|    /|\\
|     |
|    
|
|
^''')		
		elif hits == 6:
			print('''
------|
|     |
|     |
|     0
|    /|\\
|     |
|    /
|
|
^''')		
		print(''.join(wordKnown))
		letGuess = input("What letter? ")
		if letGuess not in string.ascii_letters:
			print("Not a letter")
		elif letGuess in word:
			for i in range(len(word)):
				if word[i] == letGuess:
					wordKnown[i] = letGuess+" "
		elif letGuess not in word:
			hits = hits+1
	print('''
------|
|     |
|     |
|     0
|    /|\\
|     |
|    / \\
|
|
^''')
	print("Game Over")

wordInput = input("What word? ")
hangman(wordInput)