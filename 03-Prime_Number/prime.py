import math
	
def is_prime(x):
	# A prime must be greater than 1
	if x <= 1:
		return False
	# Deal with the special case for 2
	if x == 2:
		return True
	# Get the even numbers out of the way
	if x % 2 == 0:
		return False
		
	# Find the test limit (root +1)
	limit = int(math.sqrt(x)) + 1
	
	# Loop through all the odd numbers
	for i in range (3, limit, 2):
		if x % i == 0:
			return False
	
	return True
	
a = 10000019

if is_prime(a):
	print(str(a) + " is a prime number")
else:
	print(str(a) + " is NOT a prime number")
