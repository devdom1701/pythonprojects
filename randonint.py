import random

a = input("Hejj Blud give me a number. ")
if a.isnumeric() == False:
	print("Yoooe gonna shut down now cuzz your input (ISNT A NUMBER!!!!!)")
	quit()

b = random.randint(0,int(a))
c = input("Yooo whats the randomized number??? ")

if int(c) == b:
	print("You guessed correctly~")
elif int(c) > b:
	print("Guess a lower number, try again next time!")
elif int(c) < b:
	print("Guess a higher number, bro you got it wrong pls try again.")

numfirstinput = input("Oki gimme a anotha numbah ")
if numfirstinput.isnumeric() == False:
	print("Yoooe gonna shut down now cuzz your input (ISNT A NUMBER!!!!!)")
	quit()
for i in range(0,int(numfirstinput)):
	print(i)

num2 = input("Oki gimme another number")
if num2.isnumeric() == False:
	print("Yoooe gonna shut down now cuzz your input (ISNT A NUMBER!!!!!)")
	quit()

if int(num2) % 2 > 0:
	print("Yoe numbaa odd")
else: 
	print("yoe numbaaa even")


