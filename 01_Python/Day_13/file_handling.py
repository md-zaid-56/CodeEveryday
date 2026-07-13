#Creating a file using "x" mode 
file = open("learning_log.txt","x")
file.write("Day 13 \n Learning file handling!")
file.close()

#Appending the file using "a" mode
file = open("learning_log.txt","a")
file.write("\n Completed Python Sessions")
file.close()

with open("learning_log.txt","r") as file :
    print(file.read())
    #We don't write "file.close()" in because Python automatically close the file 