#-------->Swappping Two Variables---------->
#Using Two Methods
#----->Using temp variable
#----->Using assinging variable

#---->using temp variable---->

num1=int(input("Enter your Number:"))
num2=int(input("Enter your Number:"))

print("The num1 before swapping:",num1)
print("The num2 before swapping:",num2)

temp=num1
num1=num2
num2=temp

print("The number After Swapping:",num1)
print("The number After Swapping:",num2)


#----using Assinging variable

a=10
b=20

print("The num1 before swapping:",num1)
print("The num2 before swapping:",num2)

a,b=b,a

print("The number After Swapping:",num1)
print("The number After Swapping:",num2)

