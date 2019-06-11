import random
import sys
import os
import primeNum
import cryptomath

def main():
	print('Making key files...')
	makeKeyFiles('al_sweigart', 1024)
	print('Key files made.')

def generateKey(keySize):
	p = 0
	q = 0
	print('Generating p prime...')
	print('Generating q prime...')
	while p==q:
		p = primeNum.generateLargePrime(keySize)
		q = primeNum.generateLargePrime(keySize)
	n = p * q

	print('Generating e that is relatively prime to (p-1)*(q-1)...')
	while True:
		e = random.randrange(2 ** (keySize - 1), 2 ** (keySize))
		if cryptomath.gcd(e, (p - 1) * (q - 1)) == 1:
			break

	print('Calculating d that is mod inverse of e...')
	d = cryptomath.findModInverse(e, (p - 1) * (q - 1))

	publicKey = (n, e)
	privateKey = (n, d)

	print('Public key:', publicKey)
	print('Private key:', privateKey)

	return (publicKey, privateKey)

def makeKeyFiles(name, keySize):
	if os.path.exists('{}_pubkey.txt'.format(name)) or os.path.exists('{}_privkey.txt'.format(name)):
		sys.exit('WARNING: The file {0}_pubkey.txt or {0}_privkey.txt already exists! Use a different name or delete these files and rerun this program.'.format(name))

	publicKey, privateKey = generateKey(keySize)

	print()
	print('The public key is a {} and a {} digit number.'.format(len(str(publicKey[0])), len(str(publicKey[1]))))
	print('Writing public key to file {}_pubkey.txt...'.format(name))
	fo = open('{}_pubkey.txt'.format(name), 'w')
	fo.write('{},{},{}'.format(keySize, publicKey[0], publicKey[1]))
	fo.close()

	print()
	print('The private key is a {} and a {} digit number.'.format(len(str(privateKey[0])), len(str(privateKey[1]))))
	print('Writing private key to file {}_privkey.txt...'.format(name))
	fo = open('{}_privkey.txt'.format(name), 'w')
	fo.write('{},{},{}'.format(keySize, privateKey[0], privateKey[1]))
	fo.close()

if __name__ == '__main__':
	main()
