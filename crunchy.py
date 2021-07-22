import hashlib
import sys




def insha(string):
	encoded = string.encode()
	result = hashlib.sha256(encoded)
	return result.hexdigest()



# while word != '99999999':
# 
with open('output.txt', 'w') as file:  # Use file to refer to the file object

	for i in range(99999999):
		word = str(i).rjust(8,'0')
		wordy = insha(word)
		print(word ,end='\r')
		sys.stdout.flush()
		file.write(wordy)
		file.write('\n')

print('\n')		
print(word)

