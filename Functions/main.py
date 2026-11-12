# def sum(n):
#     a=0
#     while(n>0):
#         d=n%10
#         a+=d                # sum of the digits
#         n//=10
#     return(a)

# n=int(input())
# print(sum(n))

# def count(n):
#     c=0
#     while(n>0):
#         n=n//10             # count the numbers
#         c+=1
#     return(c)

# n=int(input())
# print(count(n))

# def rev(n):
#     r=0
#     while(n>0):
#         r=r*10+n%10         # reverse
#         n//=10
#     return(r)
# n=int(input())
# print(rev(n))

# def arm(n):
#     i=0
#     a=n
#     while(a>0):
#         i+=(a%10)**3       # Armstrong Number
#         a//=10
#     return("Armstrong Number" if i==n else "Not an Armstrong Number")

# n=int(input())
# print(arm(n))

# def adam(n):
#     i=n
#     r=0
#     while(i>0):
#         r=r*10+i%10
#         i//=10
#     a=n**2                          # adams Number
#     b=r**2
#     re=0
#     while(b>0):
#         re=re*10+b%10
#         b//=10
#     return("adams number" if a==re else "not an adams number")

# n=int(input())
# print(adam(n))

























