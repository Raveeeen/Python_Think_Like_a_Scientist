#-*-coding:utf8-*-
# return value function
import math as m


def area(radius):
	# temp = m.pi * radius**2
	return m.pi*radius**2
def absolute_value(x):
	if x < 0 :
		return -x
	return x
#增量開發
def distance(x1,y1,x2,y2):
	"""the comments containing print function are called
	scaffolding code which is used as a part of constructing
	a function step by step"""
	dx = x1 - x2
	dy = y1 - y2
	# print 'dx is', dx
	# print 'dy is', dy
	dsquared = dx**2 + dy**2
	# print 'dsquared is', dsquared
	result = m.sqrt(dsquared)
	return result
# print distance(1,4,3,7)
# practice 6-2
def hypotenuse(a,b):
	return m.sqrt(a**2 + b**2)
# print hypotenuse(3,4)

#Assemble-組合
#利用前面寫好的面積和計算距離函數, 
# 可以設計一個輸入圓心和圓周上任一位置的點計算圓面積的函數
def circle_area(xc,yc,xp,yp):
	"""this function demonstrate a example for asseembling 
	a function by pre-design function with good API"""
	radius = distance(xc,yc,xp,yp)
	result = area(radius)
	print "The radius is", radius, "and the area is", result
	return result
# circle_area(0,0,3,4)
def is_divisible(a,b):
	if a%b == 0:
		return True
	return False
def is_between(a,b,c):
	if (a<b) and (a<c):
		if b<c:
			print "this is a sequential number row"
			return True
	return False
def factorial(n):
	# space = " " * (4 * n)
	# print space, 'factorial', n
	if n == 0:
		# print space, 'returnning 1'
		return 1
	# print space 
	return n*factorial(n-1)
def fibonacci(n):
	if not isinstance(n,int):
		print "please input a integer as argument"
		return False
	elif n < 0:
		print "please input a positive intger as argument"
		return False
	if n == 0:
		return 0
	if n == 1:
		return 1
 	return fibonacci(n-1) + fibonacci(n-2)
#practice 6.11

#Ackermann function 

def ack(m,n):
	if (m == 0):
		return n + 1
	elif (m > 0 and n == 0):
		return ack(m - 1, 1)
	elif (m > 0, n > 0):
		return ack(m - 1,ack(m,n-1))



