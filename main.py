# n=int(input("Enter the Year:",))
# if(n%4==0):
#     print(n,"It's a Leap Year")
# else:
#     print(n,"It is Not a Leap Year ")

# temp=int(input("Enter a value: ",))
# Hum=int(input("Enter a value: ",))
# if(temp>=30) and (Hum>=90):
#     print("Hot and Humid")
# elif(temp>=30) and (Hum<90):
#     print("Hot")
# elif(temp<30) and (Hum>=90):
#     print("Hot")
# else:
#     print("cool")

# n=int(input("Enter a Value:",))
# if(n==100):
#     print("No Charge")
# elif(n>=200):
#     print(n+150)
# elif(n>=200) and (n>=300):
#     print(n+200)
# else:
#     print("nothing")

# n=int(input())
# i=1
# while(i<=n):       Even 
#     print(i)
#     i+=2
    
# n=int(input())
# i=2
# while(n%2==0):       Odd
#     print(i)
#     i+=1
    
# n=int(input())
# i=0
# while(n>0):              
#     n=n//10              Count the Numbers
#     i+=1
# print(i)

# n=int(input())
# i=0
# while(n>0):
#     digit=n%10            sum of the digits
#     i=i+digit
#     n=n//10
# print(i)

# n=int(input())
# sum = 0
# for i in range(1,200):
#     if (i % 3 == 0) and (i % 5 == 0):   Range
#         # print(i,end=" ")
#         sum+=i
# print(sum)

# n=int(input())
# r=0
# while(n>0):
#     r=r*10+n%10                      reverse
#     n//=10
# print(r)


# n = int(input())
# a = 0
# b = 1
# #c = 2  
# for i in range(n):                  #fibanocci series
#     print(a, end=" ")
#     a, b = b, a + b
    
# n = int(input())
# s = 0
# temp = n
# while temp > 0:
#     s += (temp % 10) ** 3            #Armstrong Number
#     temp //= 10
# if s == n:
#     print("Armstrong number")
# else:
#     print("Not an Armstrong number")


# n = int(input())
# i = n
# r = 0
# while i > 0:
#     r = r * 10 + i % 10
#     i //= 10
# a = n ** 2
# b = r ** 2                             Adams Number
# re = 0
# while b > 0:
#     re = re * 10 + b % 10
#     b //= 10
# if a == re:
#     print("Adams Number")
# else:
#     print("Not an Adams Number")

# n = int(input())
# i = 0
# d = 0
# while n > 0:                           binary to decimal
#     r = n % 10
#     i += r * (2 ** d)
#     n //= 10
#     d += 1
# print(i)


# n = int(input())
# b = 0
# i = 1
# while n > 0:
#     r = n % 2                          decimal to binary
#     b += r * i
#     n //= 2
#     i *= 10
# print(b)

# n=int(input())
# i=1
# f=0
# while(i<=n):
#     if abs(i**2)-((i//2)**3)==n:       #hypher number
#         print("hyper")
#         f=1
#         break
#     i=i+1
# if(f==0):
#     print("not an hyper Number")

# def vote(a):
#     return(a>=18 and "Eligible" or "not Eligible") #vote Eligible 
# a=int(input())
# print(vote(a))

# def perfect(n):
#     a = 2
#     while a < n:
#         i, s = 1, 0
#         while i < a:
#             if a % i == 0:              # perfect number or not
#                 s += i
#             i += 1
#         if s == a:
#             print(a)
#         a += 1

# n = int(input())
# perfect(n)

# def series(n):
#     a=0
#     b=0
#     c=1
#     for i in range(n):                # tribonacci series         
#         a, b, c = b, c, a+b+c
#     return a

# n = int(input())
# print(series(n))


# def base(n, a):
#     b, i = 0, 1
#     while n > 0:
#         r = n % a
#         b += r * i            # base value
#         n //= a
#         i *= 10
#     return b

# n = int(input())
# a = int(input())
# print(base(n, a))


# def trio(n):
#     if n==0 or n==1:
#         return 0
#     elif n==2:             # another method of tribonacci series
#         return 1
#     else:
#         return trio(n-1) + trio(n-2) + trio(n-3)
# n=int(input())
# print(trio(n))

# a=input()
# b=0
# c=0
# d=0
# for i in a:
#     if i in "AEIOUaeiou":                 # vowel count
#         b+=1
#     elif i.isalpha():
#         c+=1
#     elif i.strip():
#         d+=1

# print(b,c,d,sep="-")

# s1,s2 = input().split()
# a = " "
# s1 = s1.lower()
# for c in s2:
#     if c.lower() not in s1:
#         a += c
# if a==" ":
#     print(-1)
# else:
#     print(a)
    
# a=input().split()
# b=""
# for i in a:
#     if i[0] in "AEIOUaeiou" and i[-1] in "AEIOUaeiou":      # start and end values of vowel
#         b+=i+" "
# if b:
#     print(b)
# else:
#     print(-1)


# l=[10,20,30,40]
# # print(l.pop(2))
# l.pop(1)
# print(l)

# tup=tuple("Geeks")
# print(tup[:3])

# d=[int(i) for i in input().split()]
# for i in d:
#     if(i%2==0):
#         print(oct(i))
#         # print(i[2:])
#     else:
#         print(bin(i))

# n=int(input())
# t=()
# for i in range(n):
#     a = tuple(int(j) for j in input().split())
#     a = tuple(sorted(a))
#     t += (a,)
#     print(t)

# count = 0
# for i in t:
#     if t.count(i)>1:
#         count += 1
# print(count//2)
    

# a=set(map(int,input().strip('{}').split(',')))
# b=set(map(int,input().strip('{}').split(',')))
# print(b.difference(a))
# print(a.difference(b))

# n=int(input())
# d={}
# for i in range(n):
#     a,b=input().split()
#     d.setdefault(a,[]).append(b)

# print(d)

# n=[int (i) for i in input().split(',')]
# s=[]
# for i in range(len(n)):
#     if i%2:
#         r=str(oct(n[i]))
#         s.append(r[2:])
#     else:
#         r=str(bin(n[i]))
#         s.append(r[2:])

# print(*s,sep=',')


# import calendar as c

# n=int(input())
# d=int(input())


# print(c.month(n,d))                 #import Calendar

# from datetime import datetime

# now= datetime.now()
# print(now,end=" ")



# import harshad

# n=int(input())

# for i in range(10,n+1):
#     if(i%10!=0):
#         if(harshad.harshad(i)==True):
#             print(i , end=" ")


# class cash:
#     def __init__(self,name,acc,ifsc,bal):
#         self.name = name
#         self.acc = acc
#         self.ifsc = ifsc
#         self.bal = bal
#         self.menu()
        
#     def withdraw(self):
#         n=int(input("Enter the Amount"))
#         if n <= self.bal:
#             self.bal = self.bal-n
#             print("Withdraw Successfully")
#             print("Current Balance:",self.bal)
#         self.message()
        
#     def deposit(self):
#         n = int(input("Enter the Amount:"))
#         self.bal = self.bal + n
#         print("deposit Successfully")
#         print("current Balance:",self.bal)
#         self.message()
        
#     def details(self):
#         print("Account Holder name:",name)
#         print("Account Number:",acc)
#         print("Account IFSC:",ifsc)
#         print("Account Balance:",bal)
    
#     def bal(self):
#         print("Account Balance:",self.bal)
#         self.message()
    
#     def message(self):
#         print("Thank You!!!!.......")
        
#     def menu(self):
#         while True:
#             print("\n1.withdraw")
#             print("2.deposit")
#             print("3.details")
#             print("4.Balance")
#             print("5.Exist")
            
#             m = int(input("Enter Your Choice : "))
#             match (m):
#                 case 1:self.withdraw()
#                 case 2:self.deposit()
#                 case 3:self.details()
#                 case 4:self.check_bal()
#                 case 5:break;
#                 case _:
#                     print("Invalid Number...")
#                     self.message()
#                     break
        
# c=cash("Mahesh",21,9002,100000)
        
        
        
        
    
        
            
        


        



















    












    

























 
    



    