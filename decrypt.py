import base64

ip = input("Enter input:\n")
enc = int(base64.b64decode(ip.encode("utf-8")))

mod = input("\nEnter modulus:\n")
n = int(base64.b64decode(mod.encode("utf-8")))

exp = input("\nEnter private key exponent:\n")
d = int(base64.b64decode(exp.encode("utf-8")))

dec = str(pow(enc,d,n))
if len(dec) % 3 != 0:
	dec = "0"+dec

op = "".join([chr(int(dec[i:i+3])) for i in range(0,len(dec),3)])
print("\nDecrypted:\n"+op)