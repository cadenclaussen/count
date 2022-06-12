import math

def countingWithDifferences(f, l, d):
	return math.ceil(abs(((l - f + 1)/d)))

def counting(f, l):
	return abs(l - f + 1)

def venn2(a, b, i):
	return(a+b - i)

def venn3(a, b, c, ab, ac, bc, abc):
	return(a+b+c-ab-ac-bc+abc)

def factorial(n, p):
	if n == 1:
		return p
	p *= n 
	return factorial(n - 1, p)

def withReplacement(n, r):
	return n ** r

def permutation(t, n):
	p = 1
	l = []
	for v in range(n):
		l.append(t)
		t -= 1
	return permutate(l)


def permutate(l):
	c = 1
	for number in l:
		c *= number
	return c








print(countingWithDifferences(7/8, 79/8, 3/8))
print(counting(-10, -2))
print(venn2(19, 14, 6))
print(venn3(31, 42, 37, 13, 9, 12, 4))
print(factorial(4, 1))
print(withReplacement(12, 2))
print(permutation(9, 4))
