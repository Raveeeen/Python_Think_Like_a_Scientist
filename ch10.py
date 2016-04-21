#ch10 List
def add_all(t):
	total = 0
	for x in t:
		total += x
	return total

def capitalize_all(t):
	res = []
	for s in t:
		res.append(s.capitalize())
	return res
def only_upper(t):
	res = []
	for s in t:
		if s.isupper():
			res.append(s)
	return res
def add_two_term(n):
	res = []
	for i in range(len(n)):
		if i == 0:
			res.append(n[i])
		else:
			res.append(n[i] + res[i-1])
	return res

alpha_list = []
for i in range(97,123,1):
	alpha_list.append(chr(i))
def middle(t):
	t.pop(0),t.pop(-1)
	return t
# Homework

#10-6
def is_sorted(l):
	for i in range(len(l)):
		# print 'i+1=', i+1, 'i=', i
		if i + 1 == len(l):
			return True
		if not l[i] <= l[i + 1]:
			return False
#10-7
def is_anagram(s1,s2):
	"""
	for x in s1:
		if x in s2:
			continue
		else:
			return False
	return True
	"""
	# above code is not suitable for all situation, I'll come up
	#another way to immplement it. Take advantage of built-in function
	# can make thing more clearly. The core ideal is make the string as a list and 
	#sort this list then repeat the same procedure on another string, compare both of them 
	# finally.
	str_list1 = list(s1); str_list2 = list(s2)
	str_list1.sort(); str_list2.sort()
	if str_list1 == str_list2:
		return True
	else:
		return False
def has_duplicate(a):
	s = a[:] # sort the list first
	s.sort() 
	for i in range(len(s)-1):
		if s[i] == s[i+1]:
			return True,i 
	return False
import random as rd		
def random_birth(n):
	total_list = []
	mon_date_pair = []
	for i in range(n):
		rd_mon = rd.randint(1,12)
		if rd_mon in [1,3,5,7,8,10,12]:
			rd_date = rd.randint(1,31)
		elif rd_mon in [4,6,9,11]:
			rd_date = rd.randint(1,30)
		else:
			rd_date = 28
		mon_date_pair = [rd_mon,rd_date]
		total_list.append(mon_date_pair)
	return total_list
def rd_birth_prob_test(n):
	test_times = n
	flag = 0
	for i in range(test_times):
		if has_duplicate(random_birth(23)):
			flag += 1
	return float(flag)/float(test_times)
#10-9
def has_duplicate_2(a):
	"""this version will search the item until the differcene item meet and
	return the index specifiying the exact position of each element"""
	s = a[:]
	s.sort()
	search_index = 0
	index_list = []
	# start from first element of list
	while search_index != len(s) - 1: #len(s)-1 can stop the loop at the last second element 
		j = 1 # set the increment as one
		###################################################################
		while s[search_index] == s[search_index + j]:
			if (search_index + j) == len(s) - 1: 
				break
			# this statment be putted here in case of over range of index happended in list  
			j += 1
			# if the first two is identical then move the increment until the difference meet
		###################################################################
		index_list.append(search_index)
		search_index = search_index + j 
		# search_index add j is the next start search index
		# search index is the first non-repeated index element
	"""Because we didn't check if the last two elements are identical, 
	I put a IF clause here to check the last two elements"""	
	if a[-1] != a[-2]:
		index_list.append(len(a) - 1)
	return index_list
has_duplicate_2([2,2,2])

def remove_duplicate(list_arg):
	list_get = has_duplicate_2(list_arg)
	removed_list = []
	for i in range(len(list_get)):
		removed_list.append(list_arg[ list_get[i] ])
	return removed_list		
try_removed = remove_duplicate([2,2,3,3,4,4])
print try_removed
import time as t
def read_words_1(n = 100):
	fin = open('words.txt')
	word_list = []
	for i in range(n):
		word_list.append(fin.readline().strip())
	fin.close()
	return word_list
def read_words_2(n = 100):
	fin = open('words.txt')
	word_list = []
	for i in range(n):
		word_list =  word_list + [fin.readline().strip()]
	fin.close()
	return word_list
"""
t1 = t.time()
a = read_words_1(50000)
t2 = t.time()
t3 = t2 - t1
print "%1.9f" % t3
t1 = t.time()
a = read_words_2(50000)
t2 = t.time()
t3 = t2 - t1
print "%1.9f" % t3
using append method is much faster 300 times than concatnate a list under reading 50000 strings as the list argument  
"""
def make_word_list():
	fin = open('words.txt')
	word_list = []
	for line in fin:
		word_list.append(line.strip())
	return word_list
from bisect import bisect_left
def in_bisect(s,t):
	"""review bisection search method for a sorted number array
	s: search array; t: target element; lo: lowest index; hi: highest index"""
	i = bisect_left(s,t)
	if i != len(s) and (s[i] == t or s[i+1] == t):
		# s[i+1] == t is another condition to deal in some unexpected situation that  
		# the return index is not the location where the found element is somehow it's added by extra one.
		#but it's very wired that sometimes is works well and return the correct index
		# not always though...
		return True
	else:
		return False
# when the element is not found in list, bisect_left will return a index which is 
# as the same as the length of searching list therefore it's well to use the 
# return index != len(list) as the result when you didn't find the element.

# test = raw_input("Key any word you want:\n")

# t1 = t.time(); print bisect(word_list,test); t2 = t.time(); print('%1.9f')%(t2-t1)
# t1 = t.time(); test in word_list; t2 = t.time(); print('%1.9f')%(t2-t1)

	# if len(s) == 1:
	# 	if 
	# lower_half = s[:mid]
	# higher_half = s[mid:]
	# mid = len(s)/2
 # 	return -1
 #the following code is the answer of bisection search of a word list
def reverse_pair_inner(word_list, word):
	rev_word = word[::-1]
	print rev_word
	return in_bisect(word_list,rev_word)
word_list = make_word_list()
def reverse_pair(word_list):
	rev_list = []
	for word in word_list:
		if reverse_pair_inner(word_list,word):
			rev_list.append(word)
			print word
	return rev_list
test_list = ['abc','cda','cba']
a = 'abc'
b = 'ccc'

# a = reverse_pair(word_list)

# a = reverse_pair(word_list)

# """
# following content is solution for problem 10-13 and 10-14

# def reverse_pair(word_list, word):
#     """Checks whether a reversed word appears in word_list.

#     word_list: list of strings
#     word: string
#     """
#     rev_word = word[::-1]
#     return in_bisect(word_list, rev_word)
        

# if __name__ == '__main__':
#     word_list = make_word_list()
    
#     for word in word_list:
#         if reverse_pair(word_list, word):
#             print word, word[::-1]

# def interlock(word_list, word):
#     """Checks whether a word can be split into two interlocked words.

#     word_list: list of strings
#     word: string
#     """
#     evens = word[::2]
#     odds = word[1::2]
#     return in_bisect(word_list, evens) and in_bisect(word_list, odds) 
        

# def interlock_general(word_list, word, n=3):
#     """Checks whether a word can be split into n interlocked words.

#     word_list: list of strings
#     word: string
#     n: number of interleaved words
#     """
#     for i in range(n):
#         inter = word[i::n]
#         if not in_bisect(word_list, inter):
#             return False
#     return True
        

# if __name__ == '__main__':
#     word_list = make_word_list()
    
#     for word in word_list:
#         if interlock(word_list, word):
#             print word, word[::2], word[1::2]


# #    for word in word_list:
# #        if interlock_general(word_list, word, 3):
# #            print word, word[0::3], word[1::3], word[2::3]


# """







































