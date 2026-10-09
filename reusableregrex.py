
import re

# 1. re.compile()
pattern = re.compile(r'[0-9]+')
text = "Gouri123"

result = pattern.findall(text)
print("Compile:", result)

# 2. re.finditer()
text = "My number is 9876543210"

pattern = re.finditer(r'[0-9]+', text)

print("Finditer:")
for i in pattern:
    print(i.group(), i.start(), i.end())

# 3. re.match()
text = "Python123"

result = re.match(r'Python', text)

if result:
    print("Match Found")
else:
    print("No Match")