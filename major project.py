import circle as c
import triangle as t
import rectangle as r
import square as s
import sphere as sp
import cube as cu
import cone as co
import cylinder as cy
choice=0
ch='y'
while(ch=='y'):
    print("MENU")
    print("__________________________")
    print("(1) WELCOME TO CIRCLE")
    print("(2) WELCOME TO TRIANGLE")
    print("(3) WELCOME TO RECTANGLE")
    print("(4) WELCOME TO SQUARE")
    print("(5) WELCOME TO SPHERE")
    print("(6) WELCOME TO CUBE")
    print("(7) WELCOME TO CONE")
    print("(8) WELCOME TO CYLINDER")
    print("(9) EXIT")
    print("__________________________")
    choice=int(input("Enter the choice:-"))
    if(choice==1):
        print("__________________________")
        print("(1) area of circle")
        print("(2) circumference of circle")
        print("(3) EXIT")
        print("__________________________")
        choice=0
        ch='y'
        while(ch=='y'):
            choice=int(input("Enter your choice:-"))
            if(choice==1):
                radius=eval(input("Enter the Radius of circle:-"))
                print("The Area Is:-",c.area(radius))
            elif(choice==2):
                radius=eval(input("Enter the Radius of circle:-"))
                print("The Circumfrence is:-",c.circumference(radius))
            elif(choice==3):
                print("Thank You for visiting circle")
                break
            else:
                print("ERROR:INVALID CHOICE")
    elif(choice==2):
         base=eval(input("Enter the Base of Triangle:-"))
         height=eval(input("Enter the height of triangle:-"))
         print("The Area of Triangle:-",t.area(base,height))
    elif(choice==3):
         print("___________________________")
         print("(1) Area of Rectangle")
         print("(2) Perimeter of Rectangle")
         print("(3) EXIT")
         print("___________________________")
         choice=0
         ch='y'
         while(ch=='y'):
             choice=int(input("Enter the choice:-"))
             if(choice==1):
                 w=eval(input("Enter the rectangle width:-"))
                 l=eval(input("Enter the rectangle length:-"))
                 print("The Area is:_",r.area(w,l))
             elif(choice==2):
                 w=eval(input("Enter the rectangle width:-"))
                 l=eval(input("Enter the rectangle length:-"))
                 print("The Perimeter is:-",r.perimeter(w,l))
             elif(choice==3):
                 print("THANK YOU FOR VISITING RECTANGLE")
                 break
             else:
                 print("ERROR:INVALID CHOICE")
    elif(choice==4):
         print("_________________________________")
         print("(1) Area of Square")
         print("(2) Perimeter of square")
         print("(3) Diagonal of Square")
         print("(4) EXIT")
         print("__________________________________")
         choice=0
         ch='y'
         while(ch=='y'):
             choice=int(input("Enter The Choice:-"))
             if(choice==1):
                 a=eval(input("Enter the side of Square:-"))
                 print("The area is:-",s.area(a))
             elif(choice==2):
                 p=eval(input("Enter the side of square:-"))
                 print("The Perimeter is:-",s.perimeter(p))
             elif(choice==3):
                 d=eval(input("Enter the Side of Square:-"))
                 print("The Diagonal is:-",s.diagonal(d))
             elif(choice==4):
                 print("THANK YOU FOR VISITNG SQUARE")
                 break
             else:
                 print("ERROR:INVALID CHOICE")
    elif(choice==5):
        print("___________________________________")
        print("(1) Diameter of a Sphere")
        print("(2) Surface area of a Sphere")
        print("(3) volume of Sphere")
        print("(4) EXIT")
        print("_____________________________________")
        choice=0
        ch='y'
        while(ch=='y'):
            choice=int(input("Enter the Choice:-"))
            if(choice==1):
                 d=eval(input("Enter the Sphere radius:-"))
                 print("Diameter of sphere:-",sp.diameter(d))
            elif(choice==2):
                 a=eval(input("Enter the Radius of sphere:- "))
                 print("Surface area of Sphere:-",sp.area(a))
            elif(choice==3):
                 v=eval(input("Enter the Radius of Sphere:-"))
                 print("Volme of Sphere:-",sp.volume(v))
            elif(choice==4):
                 print("THANK YOU FOR VISITING SPHERE")
                 break
            else:
                 print("ERROR:INVALID CHOICE")
    elif(choice==6):
        print("________________________________________")
        print("(1) Volume of cube")
        print("(2) Diagonal of cube")
        print("(3) Perimeter of cube")
        print("(4) EXIT")
        print("_________________________________________")
        choice=0
        ch='y'
        while(ch=='y'):
            choice=int(input("Enter the Choice:-"))
            if(choice==1):
                 l=eval(input("Enter the Length of Cube:-"))
                 b=eval(input("Enter the Breadth of Cube:-"))
                 h=eval(input("Enter the Heigth of Cube:-"))
                 print("The Volume of Cube:-",cu.volume(l,b,h))
            elif(choice==2):
                 l = eval(input("Enter the Length of Cube:-"))
                 b = eval(input("Enter the Breadth of Cube:-"))
                 h = eval(input("Enter the Heigth of Cube:-"))
                 print("Diagonal of Cube:-",cu.diagonal(l,b,h))
            elif(choice==3):
                 l = eval(input("Enter the Length of Cube:-"))
                 b = eval(input("Enter the Breadth of Cube:-"))
                 h = eval(input("Enter the Heigth of Cube:-"))
                 print("Perimeter of Cube",cu.perimeter(l,b,h))
            elif(choice==4):
                 print("THANK YOU FOR VISITING CUBE")
                 break
            else:
                 print("ERROR:INVALID CHOICE")
    elif(choice==7):
        r=eval(input("Enter the Radius of Cone:-"))
        h=eval(input("Enter the heigth of Cone:-"))
        print("Volume of Cone:-",co.volume(r,h))
    elif(choice==8):
        print("____________________________")
        print("Volume of Cylinder")
        print("Perimeter of Cylinder")
        print("Area of cylinder")
        print("EXIT")
        print("_____________________________")
        choice=0
        ch='y'
        while(ch=='y'):
            choice=int(input("Enter The Choice:-"))
            if(choice==1):
                 r=eval(input("Enter the Radius of Cylinder:-"))
                 h=eval(input("Enter the Height of Cylinder:-"))
                 print("The Volume of Cylinder:-",cy.volume(r,h))
            elif(choice==2):
                 r = eval(input("Enter the Radius of Cylinder:-"))
                 h = eval(input("Enter the Height of Cylinder:-"))
                 print("The Perimeter of Cylinder:-",cy.perimeter(r,h))
            elif(choice==3):
                 r = eval(input("Enter the Radius of Cylinder:-"))
                 h = eval(input("Enter the Height of Cylinder:-"))
                 print("The Area of Cylinder:-",cy.area(r,h))
            elif(choice==4):
                 print("THANK YOU FOR VISITING CYLINDER")
                 break
            else:
                 print("ERROR:INVALID CHOICE")
    elif(choice==9):
        print("THANK YOU FOR VISITING YAMINI'S PROJECT...HAVE A GREAT DAY")
        quit()
    else:
        print("ERROR:INVALID CHOICE")













