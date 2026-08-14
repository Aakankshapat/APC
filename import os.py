import os

print(os.name)
print(os.getcwd())
print(os.listdir("."))
try:
   os.mkdir("abc")
except FileExistsError:
     pass
         
print(os.path.exists("abc"))
print(os.path.isdir("abc"))
os.rmdir("abc")
print("directory deleted successfully")
print(os.getenv("PATH") is not None)
