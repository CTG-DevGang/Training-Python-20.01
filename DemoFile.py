#SYNTAX 

# Open file
# filename = open("filename", "mode")
# mode = r, w, a, r+, w+, a+

file1 = open("file1.txt", "r+") #r+_read and write
# Read file
#print(file1.read()) # Read all

# Read line by line
#print(file1.readline()) # Read one line

# Write file
file2 = open("file2.txt", "w") #w_write
file2.write("Hello World\n")
file2.write("DevGang")

# Close file
file1.close()
file2.close()

