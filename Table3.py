
from tabulate import tabulate


head = ["BMI category", "Health risk","weight kg"]
  

# assign data
mydata = [{"Male", 171,96 }, 
          {"Male", 161,85 }, 
          {"Male", 180,77 }, 
          {"Fema", 166,62},
          {"Fema", 150,70}, 
          {"fema", 167,82},]
  

print(tabulate(mydata))
print(tabulate(mydata,headers=head,tablefmt ='fancy_grid',showindex = True))



weight = float(input('What is your weight? ( Kg) '))
height = float(input('What is your height? ( Cm) '))
bmi = weight/(height*height)

BMI = weight / (height/100)**2

print(f"You BMI is {BMI}")

if BMI <= 18.4:
    print("You are underweight.")
    print("& Mulnutrition risk.")
elif BMI <= 24.9:
    print("You are Normal weight.")
    print("Low risk ")
elif BMI <= 29.9:
    print("You are over weight.")
    print("Enhanced risk")
elif BMI <= 34.9:
    print("You are Moderately obese.")
    print("Medium risk")
elif BMI <= 39.9:
    print("You are Severely obese.")
    print("High risk")
else:
    print("You are  Very severely obese.")
    print("Very High risk")

