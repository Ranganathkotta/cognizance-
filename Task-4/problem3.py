length=[]
a=int(input("Enter the num of records to be stored:"))

for i in range (a):
     e=input("Enter the record (Roll no, Name, Marks):")
     s=e.split()
     f=list(s)
     length.append(f)
print("Roll no", "Name", "Marks", sep='   ')
for i in length:
    print(i[0], i[1], i[2], sep='        ')
m = length[1]
print(m[0], m[1], m[2], sep='   ')