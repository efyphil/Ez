def invert_array(A:list, N:int):
	""" invert array for 0 to N-1"""
	for k in range(N//2):
		A[k], A[N-1-k] = A[N-1-k], A[k]
def test_invert_array():
	A1 = [1, 2, 3, 4, 5]
	invert_array(A1, 5)
	if A1 = [5, 4, 3, 2, 1]:
		print("test - ok")
	else:
		print("test - fail")
	A2 = [10, 0, 0 ,0 ,0 ,0, 0, 0]
		invert_array(A2, 8)
	if A2 = [10, 0, 0, 0, 0, 0, 0, 10]:
		print("test - ok")
	else:
		print("test - fail")
test_invert_array()