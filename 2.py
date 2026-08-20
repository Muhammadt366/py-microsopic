
file = open('Codingal.txt','r')
print("Reading first line...")
print(file.readline())
file.close()

file = open('Codingal.txt','r')
print("Reading multiple lines...")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()
file=   open('Codingal.txt','r')
print("looping through lines....")
for line in file:
    print(line.strip())
file.close()