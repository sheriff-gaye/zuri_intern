#-----PYTHON CALCULATOR------#
#----------------------------#
#----AUTHOR :SHERIFF GAYE ---#


#taking user inputs
x=int(input("Enter Number:"))
y=int(input("Enter NUmber :"))
operator=input("Enter an operator ie.(+, -, *, %,/ ):")

#condition to add two numbers
if operator=='+':
    print("Result", x+y)

#condition to asubtract two numbers
elif operator=='-':
    print("Result",x-y) 

#condition to multiply two numbers
elif operator=='*':
    print("Result",x*y) 

#condition for calculate the module
elif operator=='%':
    print("Result",x%y)
    
#condition to divide two numbers
else:
    print("Result",x/y)




