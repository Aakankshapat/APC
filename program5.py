user_input = int(input("Enter numbers: "))

for num in range(user_input):
    
    
    if num < 2:
        continue
        
    is_prime = True
    
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            
    if is_prime == True:
        print(num, end=" ")


