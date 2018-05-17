def array_search(A:list, N:int, x: int):
	""" search num in array A for 0 to N-1 index. 
		return index elem x in array A.
		Or -1, if it haven't find
		if in array more than 1 different elem
		return first one"""
	for k in range(N):
		if a[k] ==x:
			return k
	return -1
def test_array_search():
	A1 = [1, 2, 3, 4, 5]
	m = array_search(A1, 5, 8)
	if m == -1:
		print("#test1 - ok")
	else:
		print("test1 - fail")
	A2 = [-1, -2, -3, -4, -5]
	m = array_search(A2, 5, -3)
	if m == 2:
		print("#test1 - ok")
	else:
		print("test1 - fail")
	A3 = [10, 20, 10, 40, 50]
	m = array_search(A3, 5, 10)
	if m == 0:
		print("#test1 - ok")
	else:
		print("test1 - fail")
test_array_search()