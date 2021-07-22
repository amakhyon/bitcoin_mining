import random
import hashlib



def get_word(letters):
	word = []
	for i in range(letters):
		letter = random.randint(33,1415)
		word.append(chr(letter))
	alpha_word = ""	

	for letter in word:
		alpha_word += letter
	return alpha_word

def insha(string):
	encoded = string.encode()
	result = hashlib.sha256(encoded)
	return result.hexdigest()


def get_hash_prefixed_zeros(zeros,letters):
	while True:	
		prefix = '0' * zeros
		word = get_word(letters)
		wordy = insha(word)	
		while not wordy.startswith(prefix):
			word = get_word(letters)
			wordy = insha(word)		
		print(word)

prefix = int(input("how many zeros do you need? : "))
letters = int(input("how many letters per word? : "))
get_hash_prefixed_zeros(prefix, letters)
