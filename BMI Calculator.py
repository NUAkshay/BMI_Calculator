Height = float(input("Enter Your Height In Centimeters: "))

Weight = float(input("Enter Your Weight In Kg: "))

Height = Height/100

BMI = Weight/(Height*Height)

print("your Body Mass Index is: ",BMI)

if(BMI>0):
		
	if(BMI<=18.5):
		print("you are underweight")
		
	elif(BMI<=25):
		print("you are Healthy and Normal")
		
	elif(BMI<=30):
            
		print("you are overweight")
		
	else: print(" you are obese")
	
else:("enter valid details")
