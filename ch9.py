#-*-coding-utf8-*-
fin = open('words.txt')
# 9-1

# 
def has_no_e(word,letter = 'e'):
	if len(letter) > 1:
		return -1
	for letters in word:
		if letters == letter:
			return False
	return True
def count_line(txt_file):
	count = 0 
	for line in txt_file:
		count = count + 1
	return count
def count_e(txt_file, letter = 'e'):
	count = 0
	for line in txt_file:
		word = line.strip()
		print word
		if has_no_e(word,letter):
			count = count + 1
	return float(count)

# fin = open('words.txt')
# number_line = count_line(fin)
# fin.close()
# for i in range(97,123,1):
# 	fin = open('words.txt')
# 	chracter = chr(i)
# 	number_e = count_e(fin,chracter)
# 	percentage_e = int((float(number_e)/float(number_line))*100)
# 	print chracter, percentage_e
# 	fin.close()

def avoids(word,letter):
	if word.find(letter) == -1:
		return True
	return False
def used_only(word,cmp_list):
	for i in word:
		if (i in cmp_list):
			continue			
		else:
			print "Oops~ this vocabluary is not constituted by the letter in compare list" 
			return False
	return True
def used_all(word,cmp_list):
	"""this function can determine whether the letter in cmp_list are all appeared in word
	but it can't tell you if there are letters contained in word that doesn't existed in cmp_list
	. I will not fix the bug at this stage"""
	for i in cmp_list:
		if i in word:
			continue
		else:
			return False
	return True
def is_abecedarian(word):
	for i in range(len(word)):
	 	if i + 1 == len(word):# deal the case when meets ended charcter 
	 		break
		if ord(word[i + 1]) - ord(word[i]) <= 1 and ord(word[i + 1]) - ord(word[i]) >= 0:
			continue
		else:
			return False
	return True
# Problem set 
# 9-7

def three_pair(word):
	i_condition = 0 # used for confirm if the word satisfied the three paired letter
	j_condition = 0 # used for terminated the loop if the word is not satisfied three paired letter condtion 
	cmp_list = '' # used for checking the repeated letter
	while j_condition < len(word) - 1: # only execute untill the last second letter meet
		if word[j_condition] == word[j_condition+1]and word[j_condition] not in cmp_list:
			cmp_list = cmp_list + word[j_condition]
			i_condition = i_condition + 1		
			j_condition = j_condition + 2
			# print i_condition, j_condition 
		else:
			j_condition = j_condition + 1
			#i_condition = 0 # reset the satisfied condtion 
			# print i_condition, j_condition 
	if i_condition == 3:
		return True
	else:
		return False	
# fin = open('words.txt')
# for line in fin :
# 	if three_pair(line.strip()):
# 		print line.strip()
# 	else:
# 		pass
# 9-8 

def chkSixPalindrome(number):
	if not isinstance(number, int):
		print 'please assign a intger.'
		return False
	def is_palindrome(string):
		reverse_string = string[::-1]
		if reverse_string == string:
			return True
		return False
	number_str = str(abs(number))
	if len(number_str) != 6:
		print 'please assign a six decimal number'
	for i in [0,1,2,3]:
		if i == 0:
			number_str = str(abs(number + i))
			if not is_palindrome(number_str[2:]):
				return False
		elif i == 1:
			number_str = str(abs(number + i))
			if not is_palindrome(number_str[1:]):
				return False
		elif i == 2:
			number_str = str(abs(number + i))
			if not is_palindrome(number_str[1:5]):
				return False
		elif i == 3:
			number_str = str(abs(number + i))
			if not is_palindrome(number_str[:]):
				return False
	return True
# i = 100000
# while i < 999999:
# 	if chkSixPalindrome(i):
# 		print i
# 	i = i + 1
# the answer is 198888 and 199999
#####################################
# More clear and efficient than mine
# def has_palindrome(i, start, len):
# 	s = str(i)[start:start + len]
# 	return s == s[::-1]
# def check(i):
# 	return (has_palindrome(i,2,4) and
# 		has_palindrome(i+1,1,5) and 
# 		has_palindrome(i+2,1,4) and
# 		has_palindrome(i+3,0,6))
# i = 100000
# while i < 999999:
# 	if check(i):
# 		print i 
# 	i = i + 1
def age_diff(AgeGrandMom,AgeYou,n):
	if not(isinstance(AgeYou,int) and isinstance(AgeGrandMom,int)):
		print "Please assign an intger as the age of you or your grandmom's ages!!"
		return False
	i_condition = 0
	j_condition = 0
	diff = AgeGrandMom - AgeYou
	while i_condition < n and j_condition < 100:
		if str(AgeYou)[::-1] == str(AgeGrandMom):
			print "My grandmother is %d years old and I am %d years old." % (AgeGrandMom, AgeYou)
			i_condition = i_condition + 1
			j_condition += 1
			AgeYou += 1
			AgeGrandMom += 1
		else:
			AgeYou += 1
			AgeGrandMom += 1 
			j_condition += 1
	if i_condition == n:
		# print i_condition
		return True
	else:
		return False
# i = 9
# while not age_diff(i,0,8):
# 	i += 1
# print i
# one of the possible answer is my mom have pregnant wheb she is  9 years old which is very wired!





