#-*-coding:utf8-*-
# import string 
#你好
# def translator(frm = '',to = '',delete = '',keep = None ):
# 	if len(to) == 1:
# 		to = to*len(frm)
# 	trans = string.maketrans(frm,to)
# 	if keep is nor None:
# 		trans_all = string.maketrans('','')

def replace(s,frm,to):
	str_list = list(s)
	for i in range(len(str_list)):
		if s[i] == frm:
			str_list[i] = to # replace list element f
	result = ''
	for i in range(len(str_list)):
		result = result + str_list[i]
	return  result

def findMatchIndex(s,match):

	def str_match(s,match):
		for i in range(len(s)):
			if s[i:(i + len(match))] == match:
				return i
		return None

	i = 0
	index = []
	flag = True
	while flag:
		# match index is the index where the match string to start 
		if str_match(s[i:],match) != None:
			matchIndex = str_match(s[i:],match) + i
			print 'Match index is ', matchIndex
			index.append(matchIndex)
			nextIndex = len(match) + matchIndex 
			i = nextIndex
			print 'Next start index is ', i 
			continue
		flag = False
	return index
# print findMatchIndex('aaaapyaaapyaaapy','py')

# import string 

#單詞頻率分析
import string 
print("yo I'm a tester")
def make_dict(f): # use a text file to make a words dictionary
	words_dict = dict()
	for i in f:
		words_dict[i.strip()] = 0
	return words_dict
f = open('words.txt')
ref_dict = make_dict(f)
f.close()

# make a translator string to filter out unnecessary words
delete_trans = string.maketrans(string.uppercase + string.lowercase, ' '*(len(string.uppercase) + len(string.lowercase)))

def word_filter(s,translator = delete_trans):
	for i in range(len(translator)):
		if translator[i] != ' ':
			s = s.replace(translator[i],'')
	return s


def words_count(book,w_dict):
	for i in book:
		line = i.strip()
		# line = line.replace('\x00','') # delete \x00 character
		words_list = list()
		line = word_filter(line)
		# for punctuation in string.punctuation: # delete all
			# line = line.replace(punctuation,'')
		words_list = line.split(' ')
		# print words_list
		for j in words_list:
			# print(j)
			try:
				# print  j.lower()
				w_dict[j.lower()] = w_dict[j.lower()] + 1
				# print j.lower(), w_dict[j.lower()]
				# raw_input('find the key')
			except:
				# raw_input('did not find the key')
				# raw_input('please input a word\n')
				None
	return w_dict

def words_count_new(book):
	words_dict = dict()
	for i in book:
		line  = i.strip()
		line = word_filter(line)
		words_list = line.split(' ')
		for j in words_list:
			try:
				words_dict[j] =  words_dict[j] + 1
			except:
				words_dict.setdefault(j,1)
	return words_dict
# book = open("Book.txt")
# a = words_count(book,w_dict)
# book.close()
# book = open("Book.txt")
# b = words_count_new(book)
# book.close()

# f = open('words.txt')
# ref_dict = make_dict(f)
# f.close()
# print ref_dict == a 
def reverse_key_val(d):
	result_d = dict()
	for i in d:
		if d[i] in result_d:
			result_d[d[i]].append(i)
			# print result_d
			# print d[i] in result_d, " marked", i
		else:
			# print "marked 2"
			result_d[d[i]] = list()
			# print result_d
		# result_d[d[i]] = i
	return result_d
# a = reverse_key_val(a)
def words_count(d):
	totalNum = 0
	# for i in d:
		# totalNum = totalNum + i*len(d[i])
	for i in d: 
		totalNum = totalNum + d[i]
	return totalNum
# Num_of_Book = words_count(b)
# a.sort()	
def n_most(d,n):
	keys = d.keys()
	keys.sort()
	result = list()
	for i in range(n):
		d[keys[i]] 



# key_d = reverse_key_val(a)

# problem 13-3 ignored	
# problem 13-4  ignored

# 13-5
import random 
def choose_frm_hist(s,n = 1000):
	choice_list =  list(s)
	result_dict = dict()
	for i in range(1000):
		j = random.choice(choice_list)
		if j not in result_dict:
			result_dict.setdefault(j,0)
			continue
		result_dict[j] = result_dict[j] + 1
	return result_dict

import string 
import random 

def process_file(filename, skip_header = False):
	hist = dict()
	fp = file(filename) # instanced a file object 

	if skip_header:
		skip_gutenberg_header(fp)

	for line in fp:
		process_line(line, hist)
	return hist

def skip_gutenberg_header(fp):

	for line in fp: 
		if line.startwith('*END*THE SMALL PRINT!'):
			break 

def process_line(line, hist):

	line = line.replace('-',' ') #replace hyphens with spaces before splitting 

	for word in line.split():
		word = word.strip(string.punctuation + string.whitespace) # only remove leading and trailing character
		word = word.lower()
		word = word.replace('\x00','')	
		hist[word] = hist.get(word,0) + 1
	 # unnecessary to add a return line here because of hist will be changed globally 

def most_common(hist):

	t = list()
	for key, value in hist.items():
		t.append((value, key))

	t.sort()
	t.reverse()	
	return t # return a list

def print_most_common(hist, num = 10):
	t = most_common(hist)
	print "The most common words are:"
	for freq, word in t[:num]:
		print word,'\t', freq

def subtract(d1, d2):
	res = dict()

	for key in d1:
		if key not in d2:
			res[key] = None
	return res

def total_words(hist):
	return sum(hist.values())

def different_words(hist):
	return len(hist)  

def random_word(hist):

	t = list()
	for word, freq in hist:
		t.extend([word]*freq)

	return random.choice(t)

# import numpy as np 
# from bokeh.plotting import*
# # from bokeh.io import gridplot
# from bokeh.models import Colummn


# N = 100
# x = np.linspace(0,4*np.pi,N)
# y0 = np.sin(x)
# y1 = np.cos(x)
# y2 = np.sin(x) + np.cos(x)

# output_file("linked_panninng.html")

# s1 = figure(width=250,height=250, title='None')
# s1.circle(x, y0, size=10, color="navy", alpha=0.5)

# s2 = figure(width=250, height=250, x_range=s1.x_range, y_range=s1.y_range,title=None)
# s2.triangle(x,y1,size=10, color="firebrick", alpha=0.5)

# s3 = figure(width=250, height=250, x_range=s1.x_range,title=None)
# s3.square(x,y2,size=10, color="olive", alpha=0.5)

# p = gridplot([[s1,s2,s3]],toolbar_location=None)

# show(p)

# create two dictionary and subtract them to find out the words that don't exited in both dictionary 

"""ref_dict is the reference dictionary containing a set of regular words"""
"""book_dict is a set of words that only contain words used in book"""
book_dict = process_file("Book.txt")
diff_dict_1 = subtract(book_dict,ref_dict)
diff_dict_2 = subtract(ref_dict,book_dict)

#13-6 
set_book = set(book_dict)
set_ref = set(ref_dict)
diff_set = set_book.difference(set_ref)

#13-7 
def first_two_sum(L):
	res = []
	for i in range(len(L)):
		if i == 0: 
			res.append(L[i])
			continue
		res.append(sum(L[:(i+1)]))
	return res
print first_two_sum([5,3,31,40])

def build_freq_list(hist):
	freq_list = list(); word_list = list()
	for word in hist:
		freq_list.append(hist[word])
		word_list.append(word)
	return freq_list, word_list


def bisect_search_words(L,lower,upper,search_num):
	"""lower : the smallest index of L, 
	   upper : the highest index of L,
	   search_num : the target number in L"""
	# print "upper is ", upper
	# print "lower is", lower
	if (upper - lower) == 1:
		if L[lower] >= search_num: 
			return lower
		return upper
	mid = (lower + upper)/2 
	# print "lower is ", lower, "upper is ", upper, "mid is ", mid 	
	if search_num == L[mid]: return mid
	if L[mid] > search_num:
		return bisect_search_words(L,lower,mid,search_num)
	else:
		return bisect_search_words(L,mid,upper,search_num)

def random_choice_frm_hist(hist,n):
	res = list()
	freq_list, word_list = build_freq_list(hist)
	sum_freq = first_two_sum(freq_list)
	# print len(sum_freq), len(freq_list), len(word_list)
	total_num  = total_words(hist)
	# print total_num
	for i in range(n):
		random_num = random.randint(1,total_num)
		# print "random_num is ", random_num		
		res.append(word_list[bisect_search_words(sum_freq, 0, len(sum_freq) - 1,random_num)])
		# print word
	return res

# res = random_choice_frm_hist(book_dict,100)
# print "start random choice test"
# for i in res:
# 	print i

def sort_ordered_list(a,b):
	i,j = 0,0
	sorted_list = list()
	while i != len(a) and j != len(b):
		if a[i] < b[j]:
			sorted_list.append(a[i])
			i += 1
		else:
			sorted_list.append(b[j])
			j += 1
	if i != len(a):
		sorted_list.extend(a[i:])
	elif j != len(b):
		sorted_list.extend(b[j:])
	return sorted_list

def divine_sort(a):
	if len(a) == 1: return a
	mid = len(a)/2
	left = divine_sort(a[:mid])
	right = divine_sort(a[mid:])
	return sort_ordered_list(left,right)

# a = [13,25,27,48,51]
# b = [16,17,20,28]
# c = sort_ordered_list(a,b)

# practice 13-9
from bokeh.plotting import figure, show, output_file
import numpy as np
def Zipfs_law(hist):
	t = most_common(hist)
	y = list()
	for rank, word in t:
		y.append(rank)
	x = range(len(y))
	
	x, y = np.log10(np.array(x))[1:], np.log10(np.array(y))[1:]
	slope, intercept = fitting_Zipfs(hist)
	fitting_y = slope*x + intercept
	output_file('Zipfs_law.html', title='Zipf\'s law')
	p1 = figure(width = 500, height = 500, title='Zipf\'s law')#, x_axis_type = 'log', y_axis_type = 'log' )
	p1.circle(x,y,color='red', alpha = 1)
	p1.circle(x,fitting_y,color='navy', alpha = 1)
	# print y

	show(p)
def fitting_Zipfs(hist):
	t = most_common(hist)
	y = list()
	for rank, word in t:
		y.append(rank)
	x = range(len(y))
	x, y = np.log10(np.array(x))[1:], np.log10(np.array(y))[1:]
	A = np.vstack([x,np.ones(len(x))]).transpose()
	sol = np.linalg.lstsq(A,y)
	slope, intercept = sol[0][0], sol[0][1]
	return slope, intercept
def easy_two_dimension_plt(x,y):
	output_file('Simple plot.html', title='simple plot')
	p = figure(width = 500, height = 500, title = 'simple plot' )
	p.circle(x,y,color='dark', alpha = 1)
	# print y

Zipfs_law(book_dict)
# slope, intercept = fitting_Zipfs(book_dict)
# output_file('Simple plot.html', title='simple plot')
# p = figure(width = 500, height = 500, title = 'simple plot' )
# p.circle(x,y,color='dark', alpha = 1)
# # print y
# show(p)














