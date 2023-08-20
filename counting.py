import math

def countingWithDifferences(f, l, d):
	# Take a list with first number, last number, and the difference between each item in the list
	# For example 12, 18, 2 would return 4
	return math.ceil(abs(((l - f + 1)/d)))

def counting(f, l):
	# Counting the numbers starting at f and ending at l
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
	# Take n and r and return the number of permutations of n with replacement
	return n ** r

def permutation(t, n):
	# Take top number in the list and the number of numbers in the list and get the product
	p = 1
	l = []
	for v in range(n):
		l.append(t)
		t -= 1
	return permutate(l)


def permutate(l):
	# Called by permutate
	c = 1
	for number in l:
		c *= number
	return c


def choose(x, y):
	return factorial(x, 1)/(factorial(y, 1) * factorial(x-y, 1))



print(countingWithDifferences(7/8, 79/8, 3/8))
print(counting(-10, -2))
print(venn2(19, 14, 6))
print(venn3(31, 42, 37, 13, 9, 12, 4))
print(factorial(4, 1))
print(withReplacement(12, 2))
print(permutation(9, 4))
print(choose(6, 3))
