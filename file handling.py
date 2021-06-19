# count=0
# comp="hello everyone"+"\n"+"I m vaishnavi"+"\n"+"Python"
# file = open("C:\\Users\Asus\Desktop\\py files\\handling.txt", "w")
# file.write(comp)
# file = open("C:\\Users\Asus\Desktop\\py files\\handling.txt", "r")
# for r in file.readlines():
#     count+=1
# print(count)
# file.close()
'''

count=""
sum=0
comp="hello everyone"+"\n"+"I m vaishnavi"+"\n"+"Python"+"\n"+"Checking"+"\n"+"Done the program"
file = open("C:\\Users\Asus\Desktop\\py files\\handling.txt", "w")
file.write(comp)
file = open("C:\\Users\Asus\Desktop\\py files\\handling.txt", "r")
for r in file.readlines():
    count = 0
    for e in r:
        if e==" ":
            count+=1
    a=(count+1)
    sum=sum+a
print(sum)
file.close()
'''

'''

count=0
comp="hello everyone"+"\n"+"I m vaishnavi"+"\n"+"Python"+"\n"+"Checking"+"\n"+"Done the program"+"\n"+"hello there"
file = open("C:\\Users\Asus\Desktop\\py files\\handling.txt", "w")
file.write(comp)
file = open("C:\\Users\Asus\Desktop\\py files\\handling.txt", "r")
w=input("Enter the word")
for r in file.readlines():
    t=r.split()
    #print(t)
    for i in t:
        if i==w:
            count+=1
print(count)
file.close()'''
'''


count=0
sum=0
comp="hello everyone"+"\n"+"I m vaishnavi"+"\n"+"Python"+"\n"+"Checking"+"\n"+"Done the program"
file = open("C:\\Users\Asus\Desktop\\py files\\handling.txt", "w")
file.write(comp)
file = open("C:\\Users\Asus\Desktop\\py files\\handling.txt", "r")
for r in file.readlines():
    count=0
    for e in r:
        if e==" ":
            count+=1
    sum=sum+count
print(sum)
file.close()'''