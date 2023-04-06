#code to ask user to enter weight and height

weight = float(input("please enter your weight in KG:"))
height = float(input("please enter your height in m:"))
#formula code for bmi
bmi = weight/(height*height)
print("your bmi is:  ", round(bmi,2))

#if statement code to see if user is obese
if bmi >= 30:
    print("you are obese")

#elif statement code to see if user is overweight

elif bmi >= 25:
    print("you are overweight")

#elif statement code to see if user is normal
elif bmi >= 18.5:
    print("you are normal")

#else statement code if user is underweight
else :
      print("you are underweight")
