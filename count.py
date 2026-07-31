def count_characters(text):
    vowels = consonants = digits = spaces = special = 0
    vowel_list = "aeiouAEIOU"
    
    for char in text:
        if char.isalpha():
            if char in vowel_list:
                vowels += 1
            else:
                consonants += 1
        elif char.isdigit():
            digits += 1
        elif char.isspace():
            spaces += 1
        else:
            special += 1
            
    return vowels, consonants, digits, spaces, special

sample_string = "Hello World! 123"
v, c, d, s, sp = count_characters(sample_string)
print(f"Vowels: {v}, Consonants: {c}, Digits: {d}, Spaces: {s}, Special: {sp}")

