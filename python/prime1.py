'''
#prime numbers
s  = "prime numbers"
#max_value = eval(input('Display primes up to what value? '))
# Try values from 2 (smallest prime number) to max_value
for value in range(2, 101):
	# See if value is prime
	is_prime = True # Provisionally, value is prime
	# Try all possible factors from 2 to value - 1
	for trial_factor in range(2, value):
		if value % trial_factor == 0:
			is_prime = False # Found a factor
			break # No need to continue; it is NOT prime
	if is_prime:
			s += str(value) + ' ' # Display the prime number
print(s)
'''
#prime numbers
s  = "prime numbers"
#max_value = eval(input('Display primes up to what value? '))
# Try values from 2 (smallest prime number) to max_value
count = 0
s=""
l = []
value = 4
while count<100:
	# See if value is prime
	is_prime = True # Provisionally, value is prime
	# Try all possible factors from 2 to value - 1
	for trial_factor in range(2, value):
		if value % trial_factor == 0:
			is_prime = False # Found a factor
			value += 1
			break # No need to continue; it is NOT prime
	if is_prime:
			s += str(value) + ' ' # Display the prime number
			value += 1
			count += 1
print(s)
