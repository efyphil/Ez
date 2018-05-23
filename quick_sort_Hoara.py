def hoar_sort(A):
	if len(A) <= 1:
		return
	L = []
	M = []
	R = []
	barrier  = A[0]
	for x in A:
		if x < barrier:
			L.append(x)
		elif x== barrier:
			M.append(x)
		else:
			R.append(x)
	hoar_sort(L)
	hoar_sort(R)
	k = 0
	for x in L + M + R:
		A[k] = x
		k += 1