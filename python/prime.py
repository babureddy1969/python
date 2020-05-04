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

#even numbers
s  = "even numbers"
for i in range (2,100):
	if i%2 == 0:
		s += str(i) + " "
print(s)

#odd numbers
s  = "odd numbers"
for i in range (3,100):
	for x in range(3,100):
		if i!=x and i%x == 0 and i%2 >0:
			s += str(i) + " "
			break
print(s)
