# 
# 
#        modifying a global variabal inside a function
# 
# x=7
# def mc():
#     global x
    # x+=4             
#     print(x)
# mc()


                     #EXCEPTION
# try:
#     a=int(input("enter the 1st number:"))
#     b=int(input("Enter the 2nd number:"))
#     print(a/b)

# except:
#     print("error occured")


# try:
#     a=int(input("enter a number"))
#     b=int(input("enter 2nd number"))
#     print(a/b)
# except ValueError:
#     print("invalid input")
# except ZeroDivisionError:
#     print("not possible")


# try:
#     a=int(input("1st number:"))
#     b=int(input("2nd number:"))
#     print(a/b)
# except ValueError:
#     print('invalid input')
# except ZeroDivisionError:
#     print("not possible")
# finally:
#     print("program ended")


# a=int(input("enter your age:"))
# if a < 18:
#     raise Exception("you are not eligible")
# print("your are eligible to vote")



# try:
#     a=int(input("enter your age:"))
#     if a<18:
#         raise Exception("you are not eligible")
#     print("you are eligible")
# except Exception as b:
#     print(b)


# try:
#     a=int(input("1st number:"))
#     b=int(input("2nd number:"))
#     print("1.add")
#     print("2.subtract")
#     print("3.division")
#     print("4.multiplication")
#     n=int(input("choose a number:"))
#     if n==1:
#         print(a+b)
#     elif n==2:
#         print(a-b)
#     elif n==3:
#         print(a/b)
#     elif n==4:
#         print(a*b)
# except ValueError:
#     print("invalid input")
# except ZeroDivisionError:
#     print("not divisible by zero")



# try:
#     a=5000
#     b=int(input("enter the amount you want to withdraw:"))
#     if b>a:
#         raise Exception("insufficient balance")
#     elif b<0:
#         raise Exception("ammount cannot be negative")
#     a-=b
#     print("balance ammount is:",a)
# except Exception as c:
#     print(c)


# try:
#   a=1000
#   b=int(input("enter the quantity you want to buy:"))
#   if b<0:
#     raise Exception("quantity cannot be -ve")
#   print("Total amount is:",a*b)
# except ValueError:
#   print("invalid input")
# except Exception as c:
#   print(c)



# a=open("anandu.txt")
# print(a.read())


# with open("anandu.txt")as a:
#     print(a.read())



# with open("anandu.txt")as a:
#        for i in range(2):
#          a.readline()
        
#        print(a.read())

with open("anandu.txt") as a:
    for i in range(2):
        a.readline()
    b=a.readline()
    print(b[2:6])

# with open('anandu.txt',"a") as b:
#     b.write("\n i am anandu mc")


# with open('anandu.txt') as b:
#     print(b.read())


# with open('anandu.txt',"w") as b:
#     b.write("hello")
    
# with open("anandu.txt") as b:
#     print(b.read())
 

# ziyad=open("ziy.txt","x")
