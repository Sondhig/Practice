
import numpy as np
flag=1
x=input("Enter a Number to check if its prime ")
for y in range(int(int(x)/2)+1):
    if(y>1):
        if(int(x)%y==0):
            flag=0

if(flag==1):
    print("It is a Prime Number")
else:
    print("Not a Prime Number")       
   
    






