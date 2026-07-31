n=input("enter the n")
count1=0
count2=0
for i in range(len(str(n))):
    if n[i].islower():
        count1+=1
    else:
        count2+=1

print("count of lowercase:",count1)
print("count of uppercase:",count2)