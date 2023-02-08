
# a simple program to check if you are eligible for vaccination

age = int(input("Enter you age: "))

if age >= 18:
  are_u_pregnent = input("are you pregnent [y/n]:")
  if are_u_pregnent == 'y' or are_u_pregnent =='Y':
        print("You're not eligible to  vaccination")
  else : 
         
    taken_first_dose = input("Have you taken the first dose covid vaccine (y/n): ")
    if taken_first_dose == 'y' or taken_first_dose == 'Y':
        print("You're eligible to second dose vaccine")
    else:
        print("Visit your nearest vaccine centre first dose vaccine")
else:
    print("You are minor, Keep using mask and soap")