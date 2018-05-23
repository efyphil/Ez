def gen_numb(N:int, M:int, prefix = None):
	""" generate all number with leading numbers
		in n system (N<=10) M range"""
	prefix = prefix or []
	if M == 0:
		print(prefix)
		return
	for digit in range(N):
		prefix.append(digit)
		gen_numb(N, M-1, prefix)
		prefix.pop()
gen_numb(4,3)
def gen_bin(M:int, prefix =""):
	""" binary numbers"""
	if M == 0:
		print(prefix)
		return
	gen_bin(M-1, prefix + "0")
	gen_bin(M-1, prefix + "1")
def find(number, A):
	""" find x in A and return True if it was"""
	for x in A:
		if number == x:
			return True
		return False
def generate_permutations(N:int, M:int=-1, prefix = None):
	""" generat all permutations N numbers in M positions with prefix"""
	M = N if M ==-1 else M:# defualt N numbers in N positions
	prefix  = prefix or []
	if M == 0:
		print(prefix)
		return
	for number in range(1, N+1):
	if find(number, prefix): 
		continue
	prefix.append(number)
	generate_permutations(N, M-1, prefix)
	prefix.pop()
generate_permutations(3)