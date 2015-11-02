'''This does not work as is. I suspect it is because of an overflow,
thought I am not certain on many things in Python at this point'''

file = open("Problem13.txt", "r")
numbers = []
print ("Hi!")
for i in range(0, 50):#save numbers into a list
	numbers.append(int(file.readline()))

total = 0.0
for i in range(0, 50):#sum numbers
    total += numbers[i]

print (str(total)[:10])
file.close()