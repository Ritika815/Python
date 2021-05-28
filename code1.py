numbers = input("Provide a sequence of 3 numbers separated by commas: ") 
lv = numbers.split(",")
ts = tuple(lv)
# print(len(lv))
# print(ts)
remove_dp=set(ts)
if len(lv)>3:
    print("Enter 3 number only")
elif len(remove_dp)==3:
    print(0)
else:
    print(4-len(remove_dp))
    
    numbers = input("Provide a sequence of 3 numbers separated by commas: ") 
lv = numbers.split(",")
ts = tuple(lv)
# print(len(lv))
# print(ts)
remove_dp=set(ts)
if len(lv)>3:
    print("Enter 3 number only")
elif len(remove_dp)==3:
    print(0)
else:
    print(4-len(remove_dp))
    
    