def signature(s):
	s = list(s)
	s.sort()
	return ''.join(s)

def all_anagrams(f):
	d = {}
	for line in open(f):
		volcabulary = line.strip().lower()
		key_volcabulary = signature(volcabulary)
		if key_volcabulary not in d:
			d[key_volcabulary] = [volcabulary]
		else: d[key_volcabulary].append(volcabulary)
	return d
anagrams_set = all_anagrams('words.txt')
values =  anagrams_set.values()
l = range(len(values))
for i in range(len(values)):
	# i is a value list in dictionary 
	l[i] = (len(values[i]),values[i])
l.sort()

	 
