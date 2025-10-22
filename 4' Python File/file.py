import os
f = open("demofile.txt", "x")                           #Creating a new file
f = open("demofile.txt","w")                            #Writing file
f.write("This is a New Python File. ")
f.close()

f = open("demofile.txt","a")
f.write("New line is appending. ")
f.close()

f = open("demofile.txt","a")
f.write("We start learning python core from today! ")
f.close()

f= open("demofile.txt","a")
f.write("It is really interesting. ")
f.close()


f = open("demofile.txt","r")
print(f.read())


if os.path.exists("demofile"):
    os.remove("demofile")
else:
    print("This file does not exist")
    print(os.path)