def gcd(a, b):
	if a == b:
		return a
	elif a > b:
		return gcd(a - b, b)
	else: #a<b
		return gcd(a ,b - a)

def modif_gcd(a, b):
	if b == 0:
		return a
	else:
		return modif_gcd(b, a%b)

def ez_gcd(a,b):
	return a if b == 0 else ez_gcd(b, a%b)