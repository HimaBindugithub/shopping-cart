"""
Project Name: Shopping Cart project Using List and Dictionaries and Exception Handling
Developer   : Bindu
Date        : 2023-12-26
Description : In this project we are Capturing the Activities of the Products like Add To Cart,View Cart,Edit Cart etc.
                1.Create Products
                2.ADD To Cart
                3.View Cart
                4.Edit Cart 
                5.Clear Cart
                6.Apply Discount
                7.Get the Bill
                8.Exit The Shopping Cart

Version     : v1.0

"""

global Products
Products=[]

def display_cart():
    print("="*50)
    print("\t******Shopping Cart*******")
    print("="*50)
    print("1.Create Products")
    print("2.Add Task")
    print("3.View Tasks")
    print("4.Edit Cart")
    print("5.Clear Cart")
    print("6.Apply The Discount")
    print("7.Get The Bill")
    print("8.Exit from the Shooping Cart")
    print("-"*50)

def create_products():
    Products=[]
    Product={
            "Product_No":input("Enter The Product Number:"),
            "Product_Name":input("Enter the Product Name:"),
            "Price":int(input("Enter the Price Of the Product:")),
            "Exp_date":input("Enter the Expiry Date:"),
            "Quantity":input("Enter The Quantity Of The Product:")
    }
    # Products.append(Product)
    print(Products)
   


def add_task():
    try:
        Product=input("Enter The Product Number:")
        Product_Name=input("Enter the Product Name:")
        Price=int(input("Enter the Price Of the Product:"))
        Exp_date=input("Enter the Expiry Date:")
        Quantity=input("Enter The Quantity Of The Product:")
        Product1={"Product_No":Product,"Product Name":Product_Name,"Price":Price,"Expiry date":Exp_date,"Quantity":Quantity}
        Products.append(Product1)
        print("Product has been added successfully")
        print(Products)
        check=input("Do you need to verify the Product Details:")
        if check.upper()=='yes':
            view_cart()
    except ValueError:
        print("Exception",ValueError)


def view_cart():
    i=1
    for pro in Products:
            print("-----------------------------")
            print(pro)
            print("-----------------------------")
            for key,value in pro.items():
                print(f"{key}:{value}")
    i=i+1


def edit_cart():
    
    try:
        Product=input("Enter The Product Number:")
        Product_Name=input("Enter the Product Name:")
        Price=int(input("Enter the Price Of the Product:"))
        Exp_date=input("Enter the Expiry Date:")
        Quantity=input("Enter The Quantity Of The Product:")
        Product1={"Product_No":Product,"Product Name":Product_Name,"Price":Price,"Expiry date":Exp_date,"Quantity":Quantity}
        Product1[input("Enter the key:")]=input("Enter value:")
        print('')
        Products.append(Product1)
        print("Product Status has been Updated")
        check=input("Do you need to verify the Product Details:")
        if check.upper()=='yes' or 'y':
            view_cart()
    except ValueError as e:
        print("Exception:",e)


def clear_cart():

    print("\nThe Original Products Details in The List Dictionary Are : ", Products, end = "\n")
    clearState = input("\nDo You Want To Clear The Total Products Details (Y OR N) : ")
    if clearState == 'Y' or clearState == 'y':
        Products.clear()
        print("\nThe Elements After Clearing Are : ", Products, end = "\n")
    else:
       print("\nThe Original Products Details in The List Dictionary Are : ", Products, end = "\n")


def apply_discount():
    try:    
        Bill=int(input("Enter Total Bill Of The Product:"))
        discount=int(input("Enter The Discount Percentage On Total Bill:"))
        discountstate=input("Do You Want To Apply Discount To The Total Bill(Y or N):")
        if discountstate.upper()=="yes" or 'y':
           result=Bill-(Bill*discount/100)
           print("After Discount Is Applied To The Bill:",result)
    except ValueError as e:
        print("Exception:",e)


def get_bill():
    try:   
        Bill=int(input("Enter Total Bill Of The Product:"))
        discount=int(input("Enter The Discount Percentage On Total Bill:"))
        getstate=input("Do You Want Bill After Applying Discount(Y or N):")
        if getstate.upper()=='yes' or 'y':
          result=Bill-(Bill*discount/100)
          print("Your Total Bill is:",result)
        else:
          print("Thank you For Shopping In Our Website......")
    except ValueError as e:
        print("Exception:",e)

def main():
    loopstatus=True
    while loopstatus:
        display_cart()
        choice=int(input("Enter your choice:"))
        try:
            if choice==1:
                create_products()
            elif choice==2:
                add_task()
            elif choice==3:
                view_cart()
            elif choice==4:
                edit_cart()
            elif choice==5:
                clear_cart()    
            elif choice==6:
                apply_discount()    
            elif choice==7:
                get_bill()
            elif choice==8:    
                loopstatus=False
                print("Exiting from the Shopping Cart..GoodBye!")
                break
            else:
                print("Invalid choice,please enter your choice between[1-8]:")
            continueState=input("\nDo You Want To Continue Again(Y Or N):")
            print(' ')
            if continueState == 'N' or continueState == 'n':
                print("\nYou Requested For Process Termination...Thank You")
                loopstatus=False
        except ValueError:
            print("Please Provide Valid Choice") 

if "_init_"==main():
   main()

