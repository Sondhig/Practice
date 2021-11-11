x=input("Enter a Number that may be a Perfect Square ")
flag=0
for i in range(int(int(x)/2)+1):
    if(i*i==int(x)):
        flag=1
if(flag==1):
    print("Is a Perfect Square")
else:
    print("Not")