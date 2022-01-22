def maxFunc(A):
	max = 0
	for i in A:
		if i > max:
			max=i
	return max

A = [1, 2, 3, 4, 5, 6, 73, 8, 10, 54]
maxNum = maxFunc(A)
print(maxNum)