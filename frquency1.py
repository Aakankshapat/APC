
text = input("Enter the string: ")
char = input("Enter the character to count: ")

frequency = 0


for current_char in text:
    if current_char == char:
        frequency += 1

print(f"The character '{char}' appears {frequency} times.")

      

