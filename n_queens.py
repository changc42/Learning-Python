import sys

n = 11
board = [[0 for i in range(0,n)] for i in range(0,n)]

def print_(b):
	for i in range(0,n):
		for j in range(0,n):
			print(b[i][j], end="")
		print()
	print()

def is_safe(b, r, c):
	
	for i in range(1,c+1):
		if(c-i<0 or c-i>=n): 
			print("bad index" + str(c-i))
			sys.exit()
		if(b[r][c-i]==1): return False
		if(r+i<n):
			if(b[r+i][c-i]==1): return False
		if(r-i>=0):
			if(b[r-i][c-i]==1): return False
		
	return True

def solve(b, c, count=[0]):
	
	if(c==n):
		count[0] += 1
		print(count[0])
		print_(b)
	else:
		for i in range(n):
			if(is_safe(b, i, c)):
				b[i][c]=1
			
				solve(b, c+1, count)
				b[i][c]=0
	
solve(board, 0)
			




