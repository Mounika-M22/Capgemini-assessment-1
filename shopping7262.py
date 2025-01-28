# 5. Shopping Cart
# - Create a program to simulate a shopping cart:
# - Add items (item name and price).
# - View cart items.
# - Calculate the total price.
# - Exit.
# - Use functions and a loop to allow multiple actions.
m=[]
while(True):
    c=int(input("enter option to perform\n1.add to cart\n2.view cart items\n3. price of cart\n4.total price of cart\n"))
    match c:
        case 1:
            def add():
                my=list(input("enter items in cart\n").split())
                print(f'items added are {my}')
                
                return my
            m=add()

            exit
        case 2:
            def view():
                if len(m)==0:
                    print(f'cart is empty!')
                
                else:
                    print(f'the items are {m}')
                
            view()
            exit
        case 3:
            def prices():
                price=list(map(int,(input("enter price of item in cart\n").split())))
                print(f'the prices are {price}')
                return price
            n=prices()
        case 4:
            def total():
                total_price=sum(n)
                print(f'the total price of the cart is {total_price}')
                return total_price
            total()

            exit
        
        case _:
            print("exit")
            break

    
   
    
    
   
    