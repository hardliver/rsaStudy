import publicKeyCipher

import random
import string

def randomString(stringLength=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

if __name__ == '__main__':
	stringLength = 128
	originString = randomString(stringLength)
	print ("Random String is ", originString)

	pubKeyFilename = 'al_sweigart_pubkey.txt'
	code = publicKeyCipher.encrypt(pubKeyFilename, originString, stringLength)
	print(code)

	privKeyFilename = 'al_sweigart_privkey.txt'
	content = publicKeyCipher.decrypt(code, privKeyFilename)
	print(content)
