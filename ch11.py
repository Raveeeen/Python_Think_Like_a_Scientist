# ch11 Dictionary

# 11.1
# import time as t
# def build_words_dict(f):
# 	result_dict = dict()
# 	for i in f:
# 		result_dict[i.strip()] = ''
# 	return result_dict
# def build_words_list(f):
# 	result_list = list()
# 	for i in f:
# 		result_list.append(i.strip())	
# 	return result_list
# fin = open('words.txt')
# words_dict = build_words_dict(fin)
# fin.close()
# fin = open('words.txt')
# words_list = build_words_list(fin)
# fin.close()

# t1 = t.time(); 'hello' in words_dict; t2 = t.time(); t3 = t2 - t1
# print t3 # it's marvelous
# t1 = t.time() ;'hello' in words_list; t2 = t.time(); t3 = t2 -t1
# print t3 # slower than above 

# def histogram(s):
# 	d = dict()
# 	for c in s:
# 		if c not in d:
# 			d[c] = 1
# 		else:
# 			d[c] += 1
# 	return d
import time
def histogram(s):
	d = dict() # build a empty dictionary 
	for i in s: # indexed all characters in string
		d[i] = d.get(i,0) + 1
	return d
def print_hist(h):
	keys_list = h.keys()
	keys_list.sort()
	for c in keys_list:
		print c, h[c]

def reverse_lookup(d,v):
	for k in d:
		if d[k] == v:
			return k
	raise ValueError, 'value does not appear in the dictionary'
def reverse_lookup_2(d,v):
	ans_list = []
	for k in d:
		if d[k] == v:
			ans_list.append(k)
	return ans_list
def invert_d(d):
	inverse = dict()
	for k in d:
		val = d[k]
		# b = inverse.get(val,[]) # return val key's pair else return c
		# inverse.setdefault(val,[k])
		inverse[val] = inverse.get(val,[]) + [k] # this one doesn't look clear... 
	return inverse
known = {0:0,1:1}
def fibonacci_fast(n):
	if n in known: #before execute the function let's look up the value in dictionary first
		return known[n]
	res = fibonacci_fast(n-1) + fibonacci_fast(n-2)
	known[n] = res # if n is not in dict then evaluate it and append it in dict
	return res 
def fibonacci_normal(n):
	if n == 0: return 0
	elif n == 1: return 1
	res = fibonacci_1(n-1) + fibonacci_1(n-2)
	return res
# let's review Ackermann function A(m,n)
def Ackermann_normal(m,n):
	if m == 0: return n + 1
	elif m > 0 and n == 0: return Ackermann_normal(m-1,1)	
	elif m > 0 and n > 0: return Ackermann_normal(m-1, Ackermann_normal(m,n-1)) 
known = {}	

def Ackermann_dict(m,n):
	if ('%d,%d' % (m,n)) in known:
		return known['%d,%d' % (m,n)]
	if m == 0:
		res = n + 1 
		known['%d,%d' % (m,n)] = res 
		return res

	elif m > 0 and n == 0: 
		res = Ackermann_dict(m-1,1)
		known['%d,%d' % (m,n)] = res 
		return res	

	elif m > 0 and n > 0: 
		res = Ackermann_dict(m-1,Ackermann_dict(m,n-1))
		known['%d,%d' % (m,n)] = res
		return res 
# t1 = time.time()
# Ackermann_normal(3,7)
# t2 = time.time()
# print t2 - t1
# t1 = time.time()
# Ackermann_dict(3,7)
# t2 = time.time()
# print t2 - t1

verbose = True
def example1():
	if verbose:
		print 'Running example1'
def example2():
	global verbose
	verbose = False
count = 0
def example3():
	global count
	count += 1


#problem

#11-9
l = [1,2,3,4,5]
def has_duplicates_dict(l):
	# using orginal list method to implement this function
	# the complex order would meet n(n+1)/2 in the worst situation  
	# build a dictionary which containing the key pair consist of element and times
	# then reverse check it again 
	# the complex order is 2*n
	d = dict()
	for i in l: # build a key to times pair of a dict.
		d[i] = d.get(i,0) + 1
	for i  in d: # check if any key value larger than 2
		if d[i] >= 2:
			return True
	return False
# a = has_duplicates_dict(['a','b','c',1,2,11])
# print a
import random as rd
def birth_list_generate(n):
	ans_list = []
	for i in range(n):
		birth_dictionary  = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
		month = rd.choice(birth_dictionary.keys())
		day = rd.randrange(1,birth_dictionary[month])
		ans_list.append((month,day))
	return ans_list
birthdaylist = birth_list_generate(30)
def rotate_word(s,n):
	chr_list = list(s)
	chr_list_n = []
	ans_s = ''
	for i in chr_list:
		ord_i = ord(i)
		chr_i = chr(ord_i + n)
		chr_list_n.append(chr_i)
	for k in chr_list_n:
		ans_s = ans_s + k
	return  ans_s 
fin = open('words.txt')
def rotate_word_dict(f,n):
	rot_dict = {}
	for line in fin:
		s = line.strip()
		r_s = rotate_word(s,n)
		rot_dict[s] = r_s
	return rot_dict 
l = rotate_word_dict(fin,3)
fin.close()

# 11-11
fin = open("pronounce.txt")
def find_homophone(f):
	for l in range(126): # number 126 is the start position that I want to start 
		f.readline()
    # start to build a empty dictionary for the volcabulary to pronounciation 
	d =dict()
	for i in f:
		a = i.strip()
		b = a.split('  ',1)
		d[b[0]] = b[1]
	ans_list = [] # this list is gonna return the answer 
	for k in d:
		if len(k) <= 2: # pass the word which length is less than two 
			continue
		k_head = k[0:2]; k_tail = k[2:] # split the word by the first two and the rest 
		trial_one = k_head[0] + k_tail # produce a new word with 
		trial_two = k_head[1] + k_tail
		if d.get(trial_one) == None or d.get(trial_two) == None:
			continue
		if d.get(trial_one) == d.get(trial_two):
			ans_list.append(k)
	for line in range(len(ans_list)):
		print ' '*line,ans_list[line]
find_homophone(fin)
fin.close()



























	
# from sympy.interactive.printing import init_printing
# init_printing(use_unicode=False,wrap_line=False,no_global=False)
# from sympy.matrices import *
# import random as rd
# import sympy
# def random_matrix():
# 	a1,a2,a3,a4,a5,a6,a7,a8,a9 = sympy.symbols('a(:9)')
# 	sym_list = [a1,a2,a3,a4,a5,a6,a7,a8,a9]
# 	rd.shuffle(sym_list)
# 	row_1 = [sym_list[0],sym_list[1],sym_list[2]]
# 	row_2 = [sym_list[3],sym_list[4],sym_list[5]]
# 	row_3 = [sym_list[6],sym_list[7],sym_list[8]]
# 	M = Matrix([row_1,row_2,row_3])
# 	# M.row_insert(1,[row_2])
# 	# M.row_insert(2,[row_3])
# 	return M
# def rot_matrix():
# 	c1,c2,c3 = sympy.symbols('c(1:4)')
# 	s1,s2,s3 = sympy.symbols('s(1:4)')
# 	R1 = Matrix([[1,0,0],[0,c1,s1],[0,-s1,c1]])
# 	R2 = Matrix([[c2,0,-s2],[0,1,0],[s2,0,c2]])
# 	R3 = Matrix([[c3,s3,0],[-s3,c3,0],[0,0,1]])
# 	return R1,R2,R3
# r1,r2,r3 = rot_matrix()
# def simple_s():
# 	l1,l2,l3 = sympy.symbols('l(1:4)')
# 	m1,m2,m3 = sympy.symbols('m(1:4)')
# 	n1,n2,n3 = sympy.symbols('n(1:4)')
# 	S = Matrix([[l1,l2,l3],[m1,m2,m3],[n1,n2,n3]])
# 	S =S.T
# 	return S
# def Resistivity_M():
# 	lo_1, lo_2, lo_3, lo_4, lo_5, lo_6 = sympy.symbols('lo_(1:7)')
# 	M = Matrix([[lo_1,lo_6,lo_5],[lo_6,lo_2,lo_4],[lo_5,lo_4,lo_3]]) 
# 	return M
# s = simple_s()
# res_M_E = Resistivity_M()
# res_M_e = s*res_M_E*s.T