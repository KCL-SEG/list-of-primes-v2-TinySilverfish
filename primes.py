"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""


def primes(number_of_primes):
	list = []

	if number_of_primes < 1:
		raise ValueError("Number of primes must be greater than 0")
	
	i = 2
	while len(list) < number_of_primes:
		for j in range(2, i):
			if i % j == 0:
				break
		else:
			list.append(i)
		i += 1
	return list

print(primes(0))