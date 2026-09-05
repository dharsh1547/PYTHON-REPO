#local variable

def order():
    food = "curd rice"
    print("your order is :", food)

order()

#enclosed variable
def cart():
    discount = 10

    def checkout():
        print("applying discount", discount)
    checkout()
cart()

#global function
user_id = "dharshini1547"

def homepage():
    print("welcome to homepage", user_id)

def profile_page():
    print("welcome to profile page", user_id)
profile_page()
homepage()

#built in variables

print(__file__)  #prints the path of the file


#use case
delivery_partner ="swiggy"

def hotel():
    items ="pizza"

    def orders():
        quantity=3
        print(f"you have ordered {quantity} {items} using the partner {delivery_partner}")
    orders()
hotel()


