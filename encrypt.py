import base64

e = 65537	#standard

ip = input("Enter input:\n")
asc = int("".join([f"{ord(c):03d}" for c in ip]))

mod = input("\nEnter modulus:\n")
n = int(base64.b64decode(mod.encode("utf-8")))

enc = pow(asc,e,n)
op = base64.b64encode(str(enc).encode()).decode("utf-8")
print("\nEncrypted:\n"+op)