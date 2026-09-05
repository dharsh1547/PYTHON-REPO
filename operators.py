a=20
b=10
#arithmetic operators
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b) #round of value
print(a%b)  #reminder
print(a**b) #20*20*20

#comparison operators
x=10
y=5
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x>=y)
print(x<=y)

#logical operators
a=True
b=False
print(a and b)
print(a or b)
print(not a)

#problem
amount = 1200
tax= amount *0.18
total=amount+tax
print(total)

if total > 1000:
    discount = total*0.10
    total-= discount
print (total)

#problem 2
age = 65
student =('yes')
if age >= 60 and student == 'yes':
    print("there is discount")
else:
    print("there is no discount")


