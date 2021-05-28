T = int(input("Enter Number of Notes:"))
lst = []
if T<1:
    print("please enter valid input") 
elif T>1000000:
    print("Please Enter less input")
else:    
    for i in range(0 ,T):
        b=int(input())
        lst.append(b)
print(lst)   
my_dict = {i:lst.count(i) for i in lst}
print(my_dict)