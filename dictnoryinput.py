a={}
a["name"]=input("enter your name")
a["age"]=int(input("enter your age"))
a["place"]=input("enter your place:")

marks=[]

for i in range(5):
    b=int(input("enter the marks:"))
    marks.append(b)
a["marks"]=marks
print(a)