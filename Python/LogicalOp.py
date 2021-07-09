name = input("What is your name? ")

high_income = True
good_credit = False

# * Applicant needs BOTH high income and good credit  

if high_income & good_credit: # Logical Op & used here....and can be used as well in its place
     print("Congratulations " + name + " you are eligible for loan !!!")
else:
     print("Sorry " + name + " you are not eligible for loan !!!")



# * Applicant needs either high income or good credit  

if high_income or good_credit: # Logical Op & used here....and can be used as well in its place
     print("Congratulations " + name + " you are eligible for loan !!!")
else:
     print("Sorry " + name + " you are not eligible for loan !!!")




# * And not used here....Applicant needs both conditions to be true and NOT changes the boolen value to the other...
# ! So if the variable has boolen value of True the NOT operator will convert it to False and condition will fail and if it is False it will convert to True so the condition will be met and program will run

good_income = True
criminal_record = False
if good_income and not criminal_record:
     print("Congratulations " + name + " you are eligible for loan !!!")