#-*-coding:utf8-*-
#ch8 String 
index = 0
fruit = 'banana'
while index < len(fruit):
	letter = fruit[index]
	print letter
	index = index + 1  
def reverse_string(string):
	if not isinstance(string, str):
		print 'input a string as the parameter'
		return 0
	length = len(string)
	for i in range(1, length + 1, 1):
		print string[-i]
# prefixes = 'JKLMNOPQ'
# suffix = 'ack'

# for letter in prefixes:
# 	if letter == 'Q' or letter == 'O':
# 		letter = letter + 'u'
# 	print letter + suffix
def find(word, letter, index):
	""" word: the string be searched, letter: the sepcified search letter 
	index: the start search index"""
	if not index < len(word):
		print 'the input index is out range of input string'
		return -1
	while index < len(word):
		if word[index] == letter:
			return index
		index = index + 1
	return -1
word = 'banana'
count = 0
for letter in word:
	if letter == 'a':
		count = count + 1
print count
def count_letter(word, letter):
	if not isinstance(word,str) or not isinstance(letter,str):
		print "Both of the parameters have to be string type"
		return -1
	if len(letter) > 1:
		print 'the target character should be one alphabet'
		return -1
	count = 0
	for i in word:
		if i == letter:
			count = count + 1
	return count 
def in_both(word1,word2):
	for letter in word1:
		if letter in word2:
			print letter
def is_reverse(word1,word2):
	if len(word1) != len(word2):
		return False
	i = 0; j = len(word2) - 1
	for k in range(0,len(word1),1):
		if word1[i] != word2[j]:
			return False
		i = i + 1; j = j - 1
	return True  
"""Home work"""
# 8-10
def is_palindrome(word):
	reverse_word = word[::-1]
	if reverse_word == word:
		print "This is a palindrome"
		return -1
	print "This is not a palindrome"
	return -1
# 8-11
def any_lowercase5(s):
	for c in s:
		if not c.islower():
			return False
	return True
# 8-12
def rotate_word(word,n):
	r_word = ''
	for letter in word:
		letter_number = ord(letter) + n 
		r_word = r_word + chr(letter_number)bg
	# print "The encoded character is ", r_word
	return r_word
