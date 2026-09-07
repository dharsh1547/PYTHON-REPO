def great(name):
    print(f"hello {name}, welcome!")
great("dharshini")

def add(a,b):
    return(a+b)

result=add(1,2)
print(result)

#*args(parameters for functions)
def add(*args):
    total = 0
    for num in args:
        total += num
    return total

print(add(1,2,3))

def create_profile(**kwargs):
    print("user profile")
    for key, value in kwargs.items():
        print(f"{key}: {value}")
create_profile(name="dharshini", age=19,job="data scientist")
