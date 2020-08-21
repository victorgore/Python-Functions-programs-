#----------------------------------------------------------------------------
# Program Authour: V. Gore
# Program 1 -- Math Functions 
#----------------------------------------------------------------------------

def add(x,y):
    return (x + y)

def subtract (x, y):
    return (x - y)

def multiply (x, y):
    return (x * y)

def divide (x, y):
    return x / y

def exp (x, y):
    return x ** y

def mod (x, y):
    return x % y



print("Enter a number to select a mathematical function")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exponent")
print("6. Remainder")

print("")

# ** Algorithm Starts here **

choice = input("Enter choice (1, 2, 3, 4, 5, 6):")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if choice == '1':
    print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
    print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
    print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
    print(num1,"/",num2,"=", divide(num1,num2))

elif choice == '5':
    print(num1,"**",num2,"=", exp(num1,num2))

elif choice == '6':
    print(num1,"%",num2,"=", mod(num1,num2))

else:
    print("Invalid Option (Please try again)")