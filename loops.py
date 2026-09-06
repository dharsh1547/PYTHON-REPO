#for loop (u know the number of iteration)
names=["dharshini","ayyappan","bharathi","maheshwari"]
for test in names:
    print(test.upper())

#while loop (runs until the condition is satisfied)
correct_pin='12345'
entered_pin='1238'

while entered_pin != correct_pin:
    entered_pin= input("enter your pin:")
print("access granted")

#break statement in for
for i in range(10):
     if i == 5:
         break
     print(i)

#continue
n=[10,-5,7,-9,11]
for num in n:
    if num < 0:
        continue
    print(num)

#pass is used as a place holder for future logic
n=[10,-5,7,-9,11]
for num in n:
    pass


count = 5
while count > 0:
    print(f"countdown: {count}")
    count -= 1
print("times up!")

items =[]
while True:
    item = input("add item (type 'done' to finish):")
    if item.lower() == "done":
        break
    items.append(item)
print("items in cart:", items)