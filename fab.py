import math
def modified_fibonacci(n):     #n = 100
	result = []
	a = 0 
	b = 1
	result.append(a)
	result.append(b)
	if n < 0:
		print("input")
		return []
	elif n == 0:
		return []
	elif n == 1:
		return [a]
	else:
		for n in range(2, n):
			c = math.pow(a, 1.1) + math.pow(b, 0.5)
			result.append(c)
			a = b
			b = c
	return result	
print(modified_fibonacci(100))