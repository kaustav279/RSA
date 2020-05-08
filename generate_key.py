from math import gcd
from random import randrange,getrandbits
import base64

def miller_rabin(n,k=40):
	q = n-1
	s = 0

	while q % 2 == 0:
		s += 1
		q //= 2

	for _ in range(k):
		a = randrange(2,n-1)
		x = pow(a,q,n)
		if x == 1 or x == n-1:
			continue
		for i in range(s):
			x = pow(x,2,n)
			if x == n-1:
				break
		else:
			return False

	return True

def generate_random_prime(length=1024):
	while True:
		p = getrandbits(length)
		p |= (1 << length - 1) | 1		#setting MSB and LSB to 1
		if miller_rabin(p):
			break
	return p

def kp():
	e = 65537	#standard
	while True:
		p = generate_random_prime()
		q = generate_random_prime()
		n = p*q
		phi = (p-1)*(q-1)
		if gcd(phi,e) == 1:
			break
	d = pow(e,-1,phi)
	return (n,d)

def display_keys(nd):
	print("Modulus:")
	print(str(base64.b64encode(str(nd[0]).encode()).decode("utf-8"))+"\n")
	print("Private Key Exponent:")
	print(str(base64.b64encode(str(nd[1]).encode()).decode("utf-8")))


display_keys(kp())