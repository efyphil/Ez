def matryoshka(n):
	if n == 1:
		print('Matrosh')
	else:
		print('top matrosh n=' , n)
		matryoshka(n-1)
		print('down matrosh n=' ,n)