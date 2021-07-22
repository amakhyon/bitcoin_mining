import random
import hashlib



def get_word():
	word = []
	for i in range(8):
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


def get_hash_prefixed_zeros(zeros):
	prefix = '0' * zeros
	word = get_word()
	wordy = insha(word)	
	while not wordy.startswith(prefix):
		word = get_word()
		wordy = insha(word)		
	print(word)

prefix = int(input("how many zeros do you need? : "))
get_hash_prefixed_zeros(prefix)