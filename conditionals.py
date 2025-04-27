def good_walking_conditions(temp,cloud):
	if temp == "Hot" and cloud == "Clear":
		print("not going outside")	
	elif temp == "Temperate" and cloud == "Cloudy":
		print("not going outside")
	elif temp == "Cold" and cloud == "Cloudy":
		print("not going outside")
	elif temp == "Cold" and cloud == "Partially Cloudy":
		print("nuh uh, we aint goin outside")
	else:
		print("WE GOIN OUTSIDE GUYS!!!!!!!!!!!!!")

temp = input("hejj input a temperature in farenheight pleas ")

if temp.isnumeric() == False:
	print("Bro you gotta type in NUMBERS ONLY!!!!")
	quit()

if int(temp) < 40:
	temp = "Cold"
elif int(temp) in range(40,80):
	temp = "Temperate"
elif int(temp) > 80:
	temp = "Hot"

print("You've Chosen..." + temp)

cloud = input("Ok now input a cloudness. choose ONLY from Clear, Cloudy, and Partially Cloudy. (this is a CaSE SeNsItIvE question)")

good_walking_conditions(temp,cloud)