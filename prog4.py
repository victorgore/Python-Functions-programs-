#----------------------------------------------------------------------------
# Program Authour: V. Gore
# Program 4 -- Functions 
#----------------------------------------------------------------------------
import math
print("")
print("CALCULATIONS MENU")
print("1) AREA (SQUARE)")
print("2) AREA (RECTANGLE)")
print("3) AREA (CIRCLE)")
print("4) PERIMETER (SQUARE)")
print("5) PERIMETER (RECTANGLE)")
print("6) PERIMETER (CIRCLE)")
print("7) EXIT")

print("\n")

while(True):
    choice=int(input("INPUT MENU CHOICE (1,2,3,4,5,6 OR 7)"))

 #This program calculates the perimeter and area of a rectangle   
   #This is how the program finds the area  
    if(choice==1):
        print("You have choosen Area(SQURE): ")
        a=float(input("ENTER SIDE LENGTH: "))
        print("Area of SQUARE is: ",a*a);
    
    elif(choice==2):
        print("You have choosen AREA (RECTANGLE): ")
        w = float(input("ENTER WIDTH: "))
        h = float(input("ENTER LENGTH: "))
        print("Area of RECTANGLE is: ", w * h);

    elif(choice==3):
        print("You have choosen AREA (CIRCLE): ")
        r = float(input("ENTER RADIUS: "))
        print("Area of CIRCLE is: ",math.pi*pow(r,2));
    
  #This is how the program finds perimeter 
    elif(choice==4):
        print("You have choosen PERIMETER (SQUARE): ")
        a = float(input("ENTER SIDE LENGTH: "))
        print("Area of PERIMETER (SQUARE) is: ", 4 * a);

    elif(choice==5):
        print("You have choosen PERIMETER (RECTANGLE): ")
        w = float(input("ENTER WIDTH: "))
        h = float(input("ENTER LENGTH: "))
        print("Area of RECTANGLE is: ", 2*(w + h));
    
    elif (choice == 6):
        print("You have choosen PERIMETER (CIRCLE): ")
        r = float(input("ENTER RADIUS: "))
        print("Area of PERIMETER (CIRCLE) is: ", 2*math.pi * r);
    elif(choice==7):
       break;
