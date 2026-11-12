# math-mathmatical function

# import math

# print(math.sqrt(36))  #6.0
# print(math.pow(2,3))  #8.0
# print(math.ceil(4.3))  #5
# print(math.floor(6.9))  #6
# print(math.pi) #3.14
# print(math.factorial(5)) #120

# calendar module

# import calendar as c

# print(c.month(2026,10))  # 10 month of calender
# print(c.calendar(2026)) #2026 calender
# print(c.weekday(2026,11,1))  #(y,m,d)  (0-6)
# print(c.monthcalendar(2026,11))
# # print(c.monthrange(2026,10))



# print(d.year) #2026
# print(d.month) #11
# print(d.day) #1

# now = datetime.now()
# print(now.strftime("%d-%m-%y  %HH %mm %ss"))
# print(now.strftime("%A"))




# a=int(input())
# b=int(input())
# sum=a+b
# print(sum)

# def sum(a,b):
#     return a+b
    
# a=int(input())
# b=int(input())
# print(sum(a,b))


# import calendar as c

# n=int(input())
# d=int(input())


# print(c.month(n,d))                 #import Calendar

# from datetime import datetime

# now= datetime.now()
# print(now,end=" ")



import harshad

n=int(input())

for i in range(10,n+1):
    if(i%10!=0):
        if(harshad.harshad(i)==True):
            print(i , end=" ")










