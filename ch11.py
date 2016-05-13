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

def histogram(s):
	d = dict()
	for i in s:
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
		b = inverse.get(val,[])
		inverse.setdefault(val,[k])
		inverse[val] += [k] 
	return inverse






































	
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