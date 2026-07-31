text = input("Enter the string: ").split()
text1=[]
count=0
for i in text:
    if i not in text1:
        text1.append(i)
        count+=1
print(count)        