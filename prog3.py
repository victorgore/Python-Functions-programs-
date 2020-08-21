#----------------------------------------------------------------------------
# Program Authour: V. Gore
# Program 3 -- Loops and If Conditions
#----------------------------------------------------------------------------

password = input("Press Enter to continue")
while password != "hello":
     password = input("Password?")

name = input("What is your name?")
if name == "Victor" or name == "victor":
   print("What a great name!")
elif name == "Madona" or name == "Cher":
   print("May I have your autograph,please?")
else:
   print(name,",that's a nice name")