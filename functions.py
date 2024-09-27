import random

name = input("What is your name ")
if name.isalpha() == False:
	print("Boyooo u gotta enter text")
	quit()

def helloworld():
	print("HelloWorld")

def helloname(name):
	print("Hello " + name)

helloworld()
helloname(name)

low = input("Giev me 1 number")
high = input("Give me second numbr")

if low.isalpha() or high.isalpha() == True:
	print("Bozo stop entering text for stuff thats supposed to be number values thanks.")
	quit()
elif low > high:
	print("your first number has to be smaller than the second.")
	quit()

def printrandnum(low,high):
	print(random.randint(int(low),int(high)))
printrandnum(low,high)

radius = input("Give me a radius")
if radius.isalpha() == True:
	print("Please input integer inputs.")
	quit()
elif int(radius) < 0:
	print("Bro negative numbers aint allowed")
	quit()

def printcircumference(radius):
	print("the circuference of your circle is... ")
	print((int(radius) * 2 * 3.14))
printcircumference(radius)
