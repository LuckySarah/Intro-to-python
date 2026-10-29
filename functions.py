# functions methods
# print("Hello World") # built in
from custom_functions import greet

with open ("temp.txt", "w") as file: # w means write mode
    file.write("99.34\n") #tells the computer to run in new line
    file.write("100\n")
    file.write("54.34\n")

with open ("temp.txt", "r") as file: #r means read mode as a file
    content = file.read()
    print(content)

# pip install yt-dlp to install the library pip install yt-dlp
# to upgrade the library tun python.exe -m pip install --upgrade pip

greet()
