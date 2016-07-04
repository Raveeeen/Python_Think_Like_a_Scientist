
fin = open("pronounce.txt")
for l in range(126): # number 126 is the start position that I want to start 
	fin.readline()
d =dict()

for i in fin:
	a = i.strip()
	b = a.split('  ',1)
	d[b[0]] = b[1]
ans_list = []
for k in d:
	if len(k) <= 2:
		continue
	k_head = k[0:2]; k_tail = k[2:]
	trial_one = k_head[0] + k_tail
	trial_two = k_head[1] + k_tail
	if d.get(trial_one) == None or d.get(trial_two) == None:
		continue
	if d.get(trial_one) == d.get(trial_two):
		ans_list.append(k)
for line in range(len(ans_list)):
	print ' '*line,ans_list[line]

# for i in range(10):
# 	a = fin.readline().strip()
# 	b = a.split('  ',1)
# 	d[b[0]] = b[1]
# itr = 0
# for i in d:
# 	print ' '*itr,"Word:",i,"  Pronounce:",d[i]
# 	itr += 1