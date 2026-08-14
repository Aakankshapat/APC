




 with open("demo.txt", "w") as f:
        f.write("Initial line\n")
except Exception:
    pass

with open(filename, "r") as f:
    print("r:", f.read())

with open(filename, "wt") as f:
    print("wt works same as r")

with open(filename, "w") as f:
    f.write("Written data\n")
print("w: data written")

with open(filename, "wt") as f:
    f.write("Written wt data\n")
print("wt: data written")

with open(filename, "a") as f:
    f.write("Appended data\n")
print("a: data appended")

with open(filename, "at") as f:
    f.write("Appended at data\n")
print("at: data appended")

try:
    with open("new_demo.txt", "x") as f:
        f.write("Exclusive create")
    print("x: file created")
except FileExistsError:
    print("x: File already exists")

try:
    with open("new_demo2.txt", "xt") as f:
        f.write("Exclusive create explicit t")
    print("xt: file created")
except FileExistsError:
    print("xt: File already exists")

with open(filename, "r+") as f:
    print("r+ read:", f.read())
    f.write("r+ write\n")
print("r+ action completed")

with open(filename, "r+t") as f:
    f.write("r+t write\n")
print("r+t action completed")

with open(filename, "w+") as f:
    f.write("w+ write\n")
    f.seek(0)
    print("w+ read:", f.read())

with open(filename, "w+t") as f:
    f.write("w+t write\n")
print("w+t action completed")

with open(filename, "a+") as f:
    f.write("a+ write\n")
    f.seek(0)
    print("a+ read:", f.read())

with open(filename, "a+t") as f:
    f.write("a+t write\n")
print("a+t action completed")

with open(filename, "rb") as f:
    print("rb read:", f.read())

with open(filename, "wb") as f:
    f.write(b"Binary write\n")
print("wb action completed")

with open(filename, "ab") as f:
    f.write(b"Binary append\n")
print("ab action completed")

try:
    with open("bin_demo.txt", "xb") as f:
        f.write(b"Binary create")
    print("xb: file created")
except FileExistsError:
    print("xb: File already exists")

with open(filename, "rb+") as f:
    print("rb+ read:", f.read())

with open(filename, "wb+") as f:
    f.write(b"Binary wb+")
print("wb+ action completed")

with open(filename, "ab+") as f:
    f.write(b"Binary ab+")
print("ab+ action completed")
