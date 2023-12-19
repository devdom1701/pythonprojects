a = input("Input a String Nerd ")
if len(a) > 8:
	print("Bruh Print Up To 8 Characters")
elif len(a) < 8:
	print("Bruh Print Up To Eight Characters")
else:
	print(str(len(a)))
	print(a.upper())
	print(a.lower())
	print(a[0])
	print(a[len(a)-1])
	if a.lower() == True:
		print(a.replace("h", "j"))
	else:
		print(a.replace("H","J"))

	print(str(a[2:8]))
	print(str(a[0:3]))
	print(str(a[4:8]))

	for i in a:
		print(i)

b = input("Input a SECOND String Nerddddd")
print(str(a) + str(b))
if str(a) in str(b):
	print("True Bro the Strings  are the same")
else:
	print("Nahh Bro the strings aint the same")
