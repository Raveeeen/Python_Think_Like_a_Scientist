import math
def countdown(n):
	while (n > 0):
		print n
		n = n - 1
	print "Blastoff!!"
def sequence(n):
	while n != 1:
		print n
		if n % 2 == 0:
			n = n / 2
		else:
			n = n * 3 + 1
# while True:
# 	line = raw_input("> ")
# 	if line == 'done':
# 		break
# 	print line
# print 'Done'
def square_root(a, x = 1, epilson = 0.0000001):
	y = (float(x) + float(a/x)) / 2.0
	# print y
	if abs(a - y**2) < epilson:
		# print "the square root is ", y
		# print type(y)
		return y
	else:
		return square_root(a,y)
# problem set 
def print_square(n):
	for i in range(1,int(n),1):
		print float(i), " ", square_root(i), " ", math.sqrt(i), " ", math.sqrt(n) - square_root(n)

5
# 7-4
# while True:
# 	input_data = raw_input("Please input something or input 'done' to escape this program.\n")
# 	if input_data == 'done':
# 		break
# 	print eval(input_data)

def estimate_pi():
	"""this function can get good approximate pi value in 10 iteration within 1e-20 error deviation"""
	i = 0
	trial_pi = (2.0*math.sqrt(2)/9801)*math.factorial(4*i)*(1103+26390l*i)/((math.factorial(i))**4)*396**(4*i)
	print trial_pi
	while True:
		if i > 10: # first termination condition for over loop case
			break
		if abs(1.0/trial_pi - math.pi) < 1e-30:
			break
		else:
			print i
			i = i + 1
			# evaluate long_int first then divide it by float can prevent the error of truncation  
			long_int_buff = float(math.factorial(4*i)*(1103+26390*i))/float((math.factorial(i)**4)*(396**(4*i)))	
			trial_pi = 	trial_pi + (2*math.sqrt(2)/9801)*long_int_buff
			print 1.0/trial_pi
	print 1.0/trial_pi
	return trial_pi
pi = estimate_pi()