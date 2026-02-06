fp = open("text.txt") #open for read is by default
print(fp.read()) #reads the contents of the file
fp.close() #we close the file (not "really" needed here)

#this can also be done like this:
print("or in another way:")
with open("text.txt") as fp:
    print(fp.read())
    #the file is open in this context

#now I am no longer in the context
#read line by line and can also process:
with open("text.txt") as fp:
    for line in fp:
        print(line.capitalize(), end="")
        print(line.capitalize().rstrip())
        #"bob".capitalize().replace("o","i").center(100)