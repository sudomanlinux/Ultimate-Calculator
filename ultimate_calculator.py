
import math

print("Welcome to the ultimate calculator ")

operation=str(input("What calculation would you like to do? - DMAS, Percentage, Simplifying Fractions, root, exponent, perimeter of rectangle, perimeter of square, area of rectangle, area of square "))

if operation=="DMAS":
    num1=int(input("Enter the first number "))
    num2=int(input("Enter the second number "))
    suboperator=str(input("Enter which operator you would like to use +,-,*,/ ?" ))
    sum=num1+num2
    difference=num1-num2
    product=num1*num2
    quotient=num1/num2
    if suboperator=="+":
        print("The sum of", num1, "and", num2, "is", sum)

    elif suboperator=="-":
        print("The difference of", num1, "and", num2, "is", difference)

    elif suboperator=="*":
        print("The product of", num1, "and", num2, "is", product)

    elif suboperator=="/":
        print("The quotient of", num1, "and", num2, "is", quotient)

    else:
        print("Enter a valid operator")                    

elif operation=="Percentage":
    num=int(input("Enter the numerator "))
    den=int(input("Enter the denominator "))
    result=num/den *100
    print("The percentage is", result ,"%")

elif operation=="Simplifying Fractions":
    numerator=int(input("Enter the numerator "))
    denominator=int(input("Enter the denominator "))
    
    gcd=math.gcd(numerator, denominator)
    simplenum = numerator // gcd
    simpleden = denominator // gcd

    print("The simplest form of the fraction", numerator,"/",denominator, "is" ,simplenum,"/",simpleden)

elif operation=="root":
    root=int(input("Enter which number's root you want to find. "))
    sqroot=root**0.5
    print("The root of the number", root, "is", sqroot)

elif operation=="exponent":
    base=int(input("Enter the base. "))
    exp=int(input("Enter the exponent. "))
    solution=base ** exp
    print("The solution of", base,"^",exp, "is", solution)

elif operation=="perimeter of rectangle":
    length=int(input("Enter the Length"))
    breadth=int(input("Enter the breadth"))
    perimeter=2*length + 2*breadth
    print("The perimeter of rectangle with length", length, "and breadth", breadth, "is", perimeter)

elif operation=="perimeter of square":
    side=int(input("Enter the side of the square"))
    square=side*4
    print("The perimeter of square with side", side, "is", square)

elif operation=="area of rectangle":
    l=int(input("Enter the length of rectangle. "))
    b=int(input("Enter the breadth of rectangle. "))
    area_rec=l*b
    print("The area of rectangle with length", l, "and", b, "is", area_rec)    

elif operation=="area of square":
    side_area=int(input("Enter the side of the square. "))
    area_square=side_area**2
    print("The area of square with side", side_area, "is", area_square)