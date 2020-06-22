import math
import numpy as np
import sqlite3
import tkinter
from tkinter import *

conn = sqlite3.connect("mydatabase.db") # or use :memory: to put it in RAM
#  
cursor = conn.cursor()
#  
#create table
#cursor.execute("""CREATE TABLE albums
#                   (title text, artist text, release_date text, 
#                   publisher text, media_type text) 
#              """)
 
cursor.execute("INSERT INTO albums VALUES ('Glow', 'Andy Hunter', '7/24/2012', 'Xplore Records', 'MP3')")
conn.commit()
albums = [('Exodus', 'Andy Hunter', '7/9/2002', 'Sparrow Records', 'CD'),
        ('Until We Have Faces', 'Red', '2/1/2011', 'Essential Records', 'CD'),
        ('The End is Where We Begin', 'Thousand Foot Krutch', '4/17/2012', 'TFKmusic', 'CD'),
        ('The Good Life', 'Trip Lee', '4/10/2012', 'Reach Records', 'CD')]
cursor.executemany("INSERT INTO albums VALUES (?,?,?,?,?)", albums)
conn.commit()
cursor.execute("Select * from albums")
print("\n " , albums , end = " \n ")	


def PrimeNumber(prime):
	if prime == 1:
		print("1 is Prime Number")
		return False
	for p in range(2,prime):
		if(prime % p == 0):
			print("{} is equal to {} = {}".format(prime , p , prime//p))
			return False
		else:
			print("\n {} is prime number ".format(prime))
			return True
for series in range(2, 40):
	PrimeNumber(series)
PrimeNumber(0)	


class Fibonacci:
	def __init__(self , nos1 , nos2):
		#self.num = num
		self.nos1 = nos1
		self.nos2 = nos2
	def fibonacciNumber(self):
		#self.nos1 , self.nos2 = 0,1
		while True:
			yield self.nos2
			self.nos1 , self.nos2 = self.nos2 , self.nos1 + self.nos2
print("\n Fibonacci Series:")
fibo = Fibonacci(0 , 1)
for fib in fibo.fibonacciNumber():
	if fib > 10:break
	print(fib  , end = "  ")
print("\n")		



print("\n Swapping b/w 2 numbers")

def swappNumbers(n1 ,n2):
	n1 = n1 + n2   #->8
	n2 = n1 - n2   #->3
	n1 = n1 - n2   #->5
	return n1 , n2
a = int(input("\n Enter a First Number"))
b = int(input("\n Enter a Second Number"))
print("\n {} and {}".format(a,b))
swap = swappNumbers(a,b)
print("\n {} , {} \n {}".format(a,b,swap))	

#rint("\n Tuple in Python \n")
#tuples = (25,'Kumail Ali' , 24 , 'Zaigham Rizvi' , 26 , 'Shoaib')
#print(tuples)

#if tuples(1)<tuples(4):
#	print("\n My Name is Kumail")
#else:
#	print("\n My Name is not a Kumail")

print("\n Dictonary in Python")
dictonary = {1:'One' , 2 : 'Two' , 3 : 'Three' ,4 :'Four' , 5 : 'Five'}
for d in dictonary:
	print("\n Key {} and Value {} ".format(d , dictonary[d]))


pi = 3.14
def Circle(radius):
	return pi * radius * radius
def CircumFerence(radius):
	return 2*pi*radius*radius
def  Percentage(percet , total):
	answer = (percet/100) * total
	return answer


def CountString(str):
	cont = 0
	for c in str:
		cont = cont + 1
	return cont
print("\n Count the Strings")
print(CountString("Kumayl Ali"))


print("\n Circle {}".format(Circle(25)))
print("\n CircleFerence {}".format(CircumFerence(25)))

p = int(input("\n Enter a percent"))
t = int(input("\n Enter a total number"))
prc = Percentage(p,t)
print("\n Percentage of {} is {} = {} ".format(p,t,prc))

class Customer(object):
	"""docstring for Customer"""
	def __init__(self, name , balance):
		self.name = name
		self.balance = balance
	def WithdrawAmount(self,amount):
		if amount > self.balance:
			raise RuntimeError("\n Current balance is less than withdraw amount")
		self.balance = self.balance - amount
		return self.balance
	def DepositAmount(self,amount):
		self.balance = self.balance+amount
		return self.balance
blnc = float(input("\n Enter a total Balance"))
amnt = float(input("\n Enter a Amount"))
Kumayl = Customer("Kumayl Ali" , blnc)
Kumayl.WithdrawAmount(amnt)
print("\n Kumayl Balance = {} ".format(Kumayl.balance))		
				
Kanwal = Customer("Kanwal Fatima" , blnc)
Kanwal.DepositAmount(amnt)
print("\n Kanwal Balanace = {} ".format(Kanwal.balance))

highest= [1,2,3,4,5]
for h  in range(highest):
	print(h , end=" ")
	chk = highest[0]
	if(chk < highest[h+1]):
		chk = highest[h+1]
print("\n The Highest number of the above list = {} ".format(chk))

list = [1,3,2,1,4,5,1]
for cnt in range(1,7):
	for mode in list:
		if (list[mode] == list[mode+1]):
			temporary = list[mode]
print("\n Mode = {}".format(temporary))			

def BinarySearch(item_list , item):
	start = 0
	end = len(item_list) - 1
	found = False
	while (start <= end and not found):
		mid = (start+end)//2
		if item_list[mid] == item:
			found = True
		else:
			if item < item_list[mid]:
				end = mid-1
			else:
				end = mid+1
	return found
print("\n Binary Search\n")
bin1 = BinarySearch([1,2,5,3,7,6,8,4,9] , 8)
bin2 = BinarySearch([1,2,5,3,7,6,8,4,9] , 5) 	
print(bin1)
print(bin2)

def SequentialSearch(item_list , item):
	position = 0
	result = False
	while position < len(item_list):
		if item_list[position] == item:
			result = True
		else:
			position = position+1
	return result
print("\n Sequential Search\n")	
seq = SequentialSearch([1,8,3,6,5] , 3)
print(seq)			



#root = Tk()

#var = StringVar()
#label = Label( root, textvariable = var, relief = RAISED )

#var.set("\n ID")
#var.set("\n Name")
#var.set("ID")


#label.pack()
#root.mainloop()

