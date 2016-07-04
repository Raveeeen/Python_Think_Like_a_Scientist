def printall(*args):
	print args
def has_match(t1,t2):
	for x,y in zip(t1,t2):
		if x == y:
			return True
	return False
# i = []; e = []
# for index,element in enumerate('hello'):
# 	i.append(index); e.append(element)
# 	print index, element
# problem sets
#12-3
# refer the author code
def make_histo(s):
	d = dict()
	for c in s:
		d[c] = d.get(c,0) + 1
	return d
def most_frequent(s):
	hist = make_histo(s) # make a dict. containing frequency to character pair
	t = hist.items() # make list which element is tuple of key and values
	buf_res = []
	for char, freq in t:
		buf_res.append((freq,char)) # inverse the value and key pair
	buf_res.sort(reverse=True) # sort key value reversely
	res = []
	for freq,char in buf_res:
		res.append(char)
	return res
# res = most_frequent("helsodfjlfnscjsl")e

def cmp_tuple(a,b):
	"""accept strings as assignment"""
	a = tuple(a); b = tuple(b)
	ans = list()
	if len(a) != len(b): raise ValueError
	for i in range(len(a)):
		ans.append(a[i] == b[i])
	return ans
def is_converse(a,b):
	chk_list =  cmp_tuple(a,b)
	chk_index = 0
	for i in range(len(chk_list)-1):
		if chk_list[i] == chk_list[i + 1] and chk_list[i] == False: chk_index += 1
		print chk_index
	if chk_index == 1: return True
	return False
# print is_converse('aelpp','alepp')

# 12-6r
from time import time as t 
def make_word_dict(f):
	d = dict()
	for line in f:
		word = line.strip()
		d[word] = 0
	return d 
# def make_word_list(f):
# 	l = list()
# 	for line in f:
# 		word = line.strip()
# 		l.append(word)
# 	return l	
word_dict = make_word_dict(open('words.txt'))
word_dict['i'] = 0; word_dict['a'] = 0 # add i and a as availiable words in dictionary  

def reducible(w,quick_lookup_d,d = word_dict, display = False):
	"""
	   w : word that is going to be checked if it's reducible or not
	   quick_lookup_d : mapping words list to a dictionary increase search time
	   d :  words list scope 
	   """
	if w not in d: return False, quick_lookup_d# exclude word that doesn't exist in dictionary 
	def reducible_inner(w, d = word_dict):
		if len(w) == 1 or quick_lookup_d.get(w,False) == True: 
		# if the word exist in look up dict. or the length of it is exactly one it must be a reducible word 
			return True
		for i in range(len(w)):
			concatenate_w = w[:i] + w[i+1:] # delete the ith character in string
			if display == True:  print type(concatenate_w) ,concatenate_w, len(concatenate_w) # to this step the code is usable
			if concatenate_w in d: 
			# if concatenated word existed in d we 
			# make a deeper conditional clause to determine if len(n-1) is also a reducible word 
			# until length of word is one
				flag = reducible_inner(concatenate_w)
				if flag == True: quick_lookup_d[concatenate_w] = True
				return flag
		return False
	flag =  reducible_inner(w,d)
	if flag == True: quick_lookup_d[w] = True

	return flag, quick_lookup_d
# a,d = reducible('sprite')

def find_all_reducible_1(d):
	"""
	version 1 add dynamic programming ablity  to increase 
	effciency 
	d : map all words in dictionary 
	""" 
	lookup_dict = dict()
	for word in d:
		# print word
		flag, d = reducible(word,lookup_dict)
		lookup_dict.update(d) 
		# each loop will update lookup_dict and word once
	return lookup_dict # return dictionary containing  all reducible words in it
# a = {'sprite':0,'spite':0}	
# b = find_all_reducible_1(a)

b = find_all_reducible_1(word_dict)

def find_all_reducible_2(d):
	"""
	version 2 doesn't have dynamic programming feature thus its effciency is the worst 
	d : map all words in dictionary 
	""" 
	lookup_dict = dict()
	for word in d:
		# print word
		flag, d = reducible(word,{})
		lookup_dict.update(d) 
		# each loop will update lookup_dict and word once
	return lookup_dict # return dictionary containing  all reducible words in it
# a = {'sprite':0,'spite':0}	
# b = find_all_reducible_2(a)

