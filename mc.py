# """mylist=["apple","banana","orange"]
# list2=["mc","mc2",]
# mylist.extend(list2)
# print
# #del mylist
# #print(mylist)"""




# movie=["avatar","ironman","spiderman","batman","superman"]
# x=movie[1],movie[-1]
# print(x)
# movie[1]="drishyam"
# print(movie)

# fruit=["apple","banana","orange","mango"]
# fruit.append("strawberry")
# print(fruit)
# fruit.insert(2,"grape")
# print(fruit)



# student=["john","mike","jane","emma"]
# mark=[85,90,78,92]
# for i in student:
#  for j in mark:  
#         print(i,j)

# list=int(input("enter the  number of elements:"))
# total=[]
# five=[]
# for i in range(list):
#     num=int(input("enter the number:"))
#     total.append(num)

# for i in total:
#         if i%5==0:
#             five.append(i)

# print(total)
# print(five)
# print(len(five))


# n=int(input("how many numbers:"))
# list=[]
# five=[]
# for i in range(n):
#     num=int(input("enter the number:"))
#     list.append(num)

# for i in list:
#     if i%5==0:
#      five.append(i)
# print(list)
# print(five)
# print(len(five))

  

# n=int(input("Enter a number of elements: "))
# num=[]
# for i in range(n):
#  numbers=int(input("enter the number:"))
# num.append(numbers)
# print(num)


# n=int(input("how many number:"))
# list=[]
# new=[]

# for i in range(n):
#     value=int(input("enter the number:"))
#     list.append(value)

#     for i in list:
#       if list.count(i)==1:
#         new.append(i)
# print(list)
# print(new)
# print(len(new))



# a="anandu"
# b="mc"
# print("my name is ",a  + " and my surname is ",b )

# n=int(input("how many number-"))
# list=[]
# re=[]
# for i in range(n):
#     value=int(input("enter the numbers-"))
#     list.append(value)

# for i in list:
#     if list.count(i)>1 and i not in re:
#         re.append(i)
# print(re)

# x=("mc","aa","bb")
# new=list(x)
# new[1]="CC"
# x=tuple(new)


# print(x)

# a=int(input("how many numbers:"))
# b=[]
# for i in range(a):
#     c=int(input("enter the numbers:"))
#     b.append(c)
#     b.sort()
# d=tuple(b)


# print(d)
# print(len(d))
# print(min(d))
# print(max(d))
# print(d[-2])


# a=int(input("how many students:"))
# list1=[]
# for i in range(a):
#     mark=int(input("enter the marks:"))
#     list1.append(mark)
#     # b=sum(list1)
#     # c=b/len(list1)
#     # d=max(list1)
# e=tuple(list1)
# print(e)
# print("sum:",sum(e))
# print("average:",sum(e)/len(e))
# print("maximum:",max(e))


# a=("tea","coffee","juice")

# while True:
#     print("1.Display the tuple")
#     print("2.find he length")
#     print("3.search an element")
#     print("4.count the element")
#     print("5.exit")

#     choice=int(input("enter your choice:"))
    
#     if choice==1:
#      print(a)

#     elif choice==2:
#      print(len(a))

#     elif choice==3:
#      n=input("enter the element to search:")
#      if n in a:
#         print("element found")
#      else:
#         print("element not found")

#     elif choice==4:
#      element=input("enter the element to count:")
#      b=a.count(element)
#      print("count of",element,"is",b)

#     elif choice==5:
#      print("program exited") 
#      break


#     else:
#      print("invalid choice")


# list1=[1,2,2,3,3,4,5,5,]
# list2=set(list1)
# print(list2)
               
# set1={1,2,3,4,5}
# print("this is the set",set1)
# print("1.display the set" )
# print("2.add an element to the set")
# print("3.remove an element from the set")
# print("4.Exit")

# while True:

#  n=int(input("enter your choice:"))


#  if n==1:
#     print(set1)

#  elif n==2:
#     element=int(input("enter the element you want to add:"))
#     set1.add(element)
#     print(set1)  

#  elif n==3:
#     element2=int(input("enter the element you want to remove:"))
#     set1.remove(element2)
#     print(set1)
         
#  elif n==4:
#     print("progrram ended")
#     break

# else:
#    print("invalid choice")


# dance={"amina","rahul","john","sara"}
# music={"sara","john","david","ali"}

# both=dance&music
# only_one=dance-music
# print(both)
# print(only_one)
# print(dance|music)


# n=input("Enter the sentence:")
# a=n.split()
# b=set(a)
# print(b)

# n=input("enter the word:")
# n2=input("enter the 2nd word:")
# a=set(n)
# b=set(n2)
# print(a&b)

# vowels={"a","e","i","o","u"}
# n=input("enter a string:")
# a=""
# for i in n:
#     if i not in vowels:
#         a+=i
# print(a)
       

# list1=[1,2,3,3,4,5,5]
# list2=set(list1)

# print(min(list1))
# print(max(list1))



# a=set()
# for i in range(21):
#     if i%2==0:
#         a.add(i)
# print(a)


# a=input("enter the words:")
# vowels=("a","e","i","o","u")
# b=[]
# for i in a:
#     # for j in vowels:
#         if i  in vowels:
#             b.append(i)
# print(len(b))
    

# students={"name":"anandu","age":"21","course":"bca",}
# print(students["name"])
# students["grade"]='A'
# print(students)


# car={"brand":"Toyota","model":"Innova","year":2020}
# x=car.values()
# print(x)
# car["year"]="2030"
# # print(car)
# car["color"]="black"
# print(car)
# for i in car.keys():
#     print(i)

# marks={"anu":"45","athul":"43","anandu":"48"}
# marks["vishnu"]="50"
# marks.pop("athul")
# print(marks)

# person={"name=":"ameer","age=":"30","city=":"ernakulum"}
# person.get("age=")
# person.pop("city=")
# person["profession="]="engineer"
# for i ,j in person.items(): 
#     print(i,j)


# mc=dict()
# mc.update({"apple":10,"banana":25,"orange":15})
# mc["banana"]+=5
# mc.pop("orange")
# print(mc)

# def add(a,b):
#     return (a*b,)


# c=int(input("enter the 1st number"))
# d=int(input("enter the 2nd number"))
# print (add(c,d))


# def odd_even(n):
#     if n%2==0:
#         return "even"
    
#     else:
#         return "odd"
    
# n=int(input("enter the number:"))
# print(odd_even(n))
# a=int(input("how many numbers"))
# list1=[]

# for i in range(a):
#     b=int(input("enter the numbers"))
#     list1.append(b)
# # print(list1)
# def total():
#     return sum(list1)
# print(total())


# n= input("enter the string:")
# def length(n):
#     return len(n)
# print(length(n))


# n=int(input("enter the number"))
# def squre(n):
#     return n**2
# print(squre(n))


# n=int(input("enter the number"))
# def oe(n):
#     if n%2==0:
#         return "even"
#     else:
#         return "odd"
# print(oe(n))


# n=int(input("enter the first number:"))
# m=int(input("enter the second number:"))
# def larg(n,m):
#     return max(n,m)

# print(max(n,m))


# vowels=("a","e","i","o","u")
# n=str(input("enter the string:"))
# def nonvowels(n):
#  a=0

#  for i in n:
#     if i in vowels:
#      a+=1
#  return a

# print(nonvowels(n))


# n=input("Enter the string")
# def up(n):
#     a=0
#     b=0
#     for i in n:
#         if i.isupper():
#             a+=1
#         elif i.islower():
#             b+=1
#     print(a)
#     print(b)
# up(n)

    
# def num(*numbers):
#     return sum(numbers)

# print(num(1,2,3,5))
# print(num(23,45,67,123,456))    
    

# def num(*numbers):
#     numbers=int(input("enter how many numbers"))
#     b=[]
#     for i in range(numbers):
#         a=int(input("enter the number"))
#         b.append(a)

#     if len(b)==0:
#         return "none"
#     max_num=b[0]
#     for i in b:
#         if i > max_num:
#             max_num=i
#     return max_num
# print(num(1,2,3,4,56,7))

# n=(1,2,3,4,5,6,7,8,9,10)

# for i in (n):
    
#     if i==5:
#         break
#     print(i)


# m=int(input("enter the number"))
# n=[10,25,30,45,50,65]
# for i in n:
#  if i==m:
#   print("number found")
#   break
# else:
#  print("number not found")



# n=int(input("enter how many"))
# a=[]
# for i in range(n):
#     m=int(input("enter the number"))
#     a.append(m)
# for i in (a):
#  if i%2==0:
#   print(i)
#   break
    
# pas=""
# while pas!="python123":
#     pas=input("Enter the password:")
# print("Login succesful")
    

# while True:
#     pas=input("Enter the password:")
#     if pas=="python123":
#         print("login succesful")
#         break

# for i in range(10):
#    if i*7 >35:
#       break
#    print(f"{i} x 7 = {i*7}")


# a=input("enter the string:")
# b=len(a)
# rev=""
# for i in range(b-1,-1,-1):
#     rev+=a[i]
# print(rev)


# a=input("enter a string:")
# b=len(a)
# rev=""
# for i in range(b-1,-1,-1):
#     rev+=a[i]
# if rev==a:
#     print("it is a palindrom")
# else:
#     print("not a palindrom")

# a=int(input("how many numbers:"))
# # d=()
# # c=list(d)
# c=[]
# for i in range(a):
#     b=int(input("enter the numbers:"))
#     c.append(b)
# for i in range(len(c)):
#     if c[i]%2==0 and c[i]%7==0:
#         c[i]="#" 
#     elif c[i]&7==0:
#         c[i]="%"
#     elif c[i]%2==0:
#         c[i]="&"
# # d=tuple(c)
# print(c)


# a=int(input("how many numbers:"))
# b=[]
# for i in range(a):
#     c=int(input("enter the numbers:"))
#     b.append(c)
# print("original list=",b)
# for i in range(len(b)):
#     if b[i]%2!=0:
#         b[i]="&"
# print("replaced list=",b)
# e=[]

# for i in range(a-1,-1,-1):
#    e.append(b[i])
# b.reverse()   = we can also reverse list using built in key "reverse()"
# print(b)

        
# print("reversed list=",e)



# a=int(input("how many number:"))
# b=[]
# d=[]
# for i in range(a):
#     c=int(input("enter the numbers"))
#     b.append(c)
# max_count=0
# for i in b:
#     if b.count(i) > max_count:
#         max_count= b.count(i)
# print(max_count)

# for x in b:
#     if b.count(x)== max_count and x not in d:
#         d.append(x)
# print(d)
    

#      if b.count(i)>1:
#       d.append(i)
# print(b)


# a=int(input("enter the number"))
# b=1
# for i in range(1,a+1):
#     b*=i
# print(b)

# a=int(input("Enter the number:"))
# if a<2:
#    print(a,"is not prime")
# else:
#  for i in range(2,a):
#     if a%i==0:
#         print(a,"is not a prime number")
#         break
#  else:
#   print(a,"is prime number")
    
# a=input("Enter the string:")
# p=["!","@","#","$","%","^","&","*",".",",","/",":",":",";"]
# c=str()
# for i in a:
#     if i not in p:
#         c+=i
# print(c)


# a=input("enter the string:")
# b=str()
# for i in a:
#  if i.isalnum():
#   b+=i
# print(b)

# a=int(input("Enter the number of patients"))
# while True:
#  if a>20:
#   e=0
#   for i in range(a):
#    b=int(input("Enter the age of the patients "))
#    while b<120:
#      if b <17:
#        e+=200
#      elif b>17 and b<40:
#        e+=400
#      elif b>40:      this program is wrong ,contiues loop happens
       
#        e+=300
#      print(e)
#   else:
#      print("invalid age")
    
#      break
#  else:
#   print("The doctor a consult a maximum of 20 patient a day")
#   break






# a=int(input("Enter how many patients:"))
# earn=0
# if a>20:
#     print("The doctor consult a maximum of 20 patient a day")
#     exit()
# for i in range(a):
#     age=int(input("Enter the age of the patient:"))
#     if age<=0 or age > 120:
#         print("invalid age")
#         exit()
#     elif age<17:
#         earn+=200
#     elif age<40 and age>17:
#         earn+=400
#     elif age>40:
#         earn+=300
# print("total earning=",earn)

user =int(input("Enter the number:"))
a=0
b=1
print("The fibanocci numbers is:")
for i in range(user):
    print(a,end=" ")
    c=a+b
    a=b
    b=c




  


        
    


   


         

     
     
   
    


    


    

    



    





