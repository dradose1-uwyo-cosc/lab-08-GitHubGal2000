# Colin Peters
# UWYO COSC 1010
# 11/06/24
# Lab 08
# Lab Section: 15
# Sources, people worked with, help given to: Jed 
# your
# comments
# here


# Write a function that will properly check strings to see if they are an int or float, and convert them if so
# If they can't be converted return false
# Other wise return the converted int or float 
# Floats should only have one decimal point in them 
#if x == float:


def str_check(str_input):
    try:
        output = int(str_input)
        print(output)
        return output
    except ValueError:
        try:
            output = float(str_input)
            print(round(output, 1))
            return (round(output, 1))
        except ValueError:
            print(False)

print("*" * 75)
str_check(str_input = input("Whats your input? "))

###############
print("*" * 75)
###############


# Point-slope y = mx + b
# This is used in mathematics to determine what the value y would be for any given x
# Where b is the y-intercept, where the line crosses the y-axis (x = 0)
# m is the slope of the line, the rate of change, how steep the line is
# x is the variable, and is determined by which point on the graph you wish to evaluate
# Create a function slope_intercept that takes in four parameters
    # m, the slope
    # b, the intercept
    # a lower x bound
    # an upper x bound
# Return a list for all values of y for the given x range, inclusive (whole number X's only)
# Check to make sure that the lower bound is less than or equal to the upper bound
# m, b can be floats or integers
# the bounds must be integers, if not return false
# Create a while loop to prompt users for their input for the four variables
# Exit on the word exit
# Remember all inputs are strings, but the function needs ints or floats
# Call your function and print the resulting list

while True:
    mval = str_check(input("Whats your slope?"))
    bval = str_check(input("Whats your Y intercept?"))
    x_low = str_check(input("Whats your lower X bound? "))
    x_up = str_check(input("Whats your upper X bound? "))
    yval = ()
    list = []
    def slope_intercept(mval, bval, x_low, x_up):
        if x_up >= x_low:
            while x_up > x_low:
                yval = int(mval * x_up + bval)
                list.append(yval)
                x_up -= 1
            print(list)

    fg = input("break?")
    slope_intercept(mval, bval, x_low, x_up)

    if fg == "yes":
        break


###############
print("*" * 75)
###############


# Write a function to solve the quadratic formula
# https://en.wikipedia.org/wiki/Quadratic_formula
# Accept inputs for a, b, c
# Remember that this returns two values
# Create a loop like above to prompt the user for input for the three values
# Create a second function that just does the square root operation 
    # If the number you are trying to take the square root of is negative, return null

#x = (-b +- sqrt(b^2-4*a*c))/2*a

while True:
    def sqrt_check(t):
        if t < 0:
            print("give a positive")
        else:
            t = t ** .5
            return t
    a = str_check(input("Type in the value of a: "))
    b = str_check(input("Type in the value of b: "))
    c = str_check(input("Type in the value of c: "))
    x1 = ()
    x2 = ()
    def quadratic_formula(a, b, c):
        x1 = str_check(-b + sqrt_check(b*b -4*(a*c)))/(2*a)
        x2 = str_check(-b - sqrt_check(b*b -4*(a*c)))/(2*a)
        print(f"x1 is {x1}")
        print(f"x2 is {x2}")
    quadratic_formula(a, b, c)
    rgr = input("break?")
    if rgr == "yes":
        break


