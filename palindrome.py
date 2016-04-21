def first(word):
	if isinstance(word,str):
		return word[0]
	print "input a string please" 
def last(word):
	if isinstance(word,str):
		return word[-1]
def middle(word):
	if isinstance(word, str):
		return word[1:-1]
	print "input a string please"
def palindrome(word):
	if not isinstance(word, str): # type check 
		print "the input is not a string"
		return -1
	elif len(word) == 0: # exclude the empty string case
		print "the input is an empty string"
		return -1
	def is_palindrome(word):
		# Reach this condition only if the input argument is a palindrome
		if len(word) == 0: 
			print "this is a palindrome"
			return  1
		first_word = first(word)
		last_word = last(word)
		# Once the first word is not the same as the last word, the argument is not a palindrome
		if (first_word != last_word):
			print "This is not a palindrome"
			return -1
		# continue testing the middle string 
		else:	
			is_palindrome(middle(word))
	is_palindrome(word)
# pass problem 6-7

# GCD Calculation 
def gcd(a,b):
	def inner_gcd(a,b):
		if (b == 0):
			print "The GCD is ", a 
			return a
		r = a%b
		gcd(b,r)
	if (a < b):
		c = a; a = b; b = c
	inner_gcd(a,b)
# def gcd(a,b):
# 	if a < b:
# 		print "a should larger than b"
# 		return -1
# 	if (b == 0):
# 		print "The GCD is ", a 
# 		return a
# 	r = a%b
# 	gcd(b,r)

