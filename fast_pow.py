# a^n == a^(n-1) * a
def pow1(a:float, n:int):
	if n == 0:
		return 1
	elif n%2 == 1:
		return pow1(a, n - 1) * a
	else: 
		return pow(a**2 , n//2)
	