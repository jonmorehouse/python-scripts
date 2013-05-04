#!/usr/bin/python
from math import sqrt, ceil

# what is a prime number?
# No divisor possible -- trial division 
# trial division algorithm:

# 1.) Find square root
# 2.) Divide number by each number from 0->square root

def check_prime(input):


	if input == 0: return False

	# initialize edge cases etc
	if input == 1: return True

	# now create the square root to help with calculation
	# round it up and ensure that we are working with an integer
	ceil = int(sqrt(input)) + 1

	# now we need to test if we have a prime
	for i in range(2, ceil):

		if input % i == 0:
			return False	

	# return true for the primality of this number etc
	return True

primes = []

for number in range(1000):

	if check_prime(number):
		primes.append(number)

print primes




