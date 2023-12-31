"""
Project Name: Shopping Cart project Using List and Dictionaries and Exception Handling
Developer   : Bindu
Date        : 2023-12-26
Description : In this project we are Capturing the Activities of the Products like Add To Cart,View Cart,Edit Cart etc.
                1.Create Products
                2.Add To Cart
                3.View Cart
                4.Edit Cart 
                5.No of visitors to the product
                6.Clear Cart
                7.Apply Discount
                8.Get the Bill
                9.Purchased date of the product
                10.Return The Product
                11.Exchange The Product
                12.Delivery
                13.Exit The Shopping Cart

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
    print("5.No Of Visitors To The Product")
    print("6.Clear Cart")
    print("7.Apply The Discount")
    print("8.Get The Bill")
    print("9.Purchased Date Of The Product")
    print("10.Return The Product")
    print("11.Exchange the product")
    print("12.Delivery")
    print("13.Exit from the Shopping Cart")
    print("-"*50)

def create_products():
    Product={
            "Product_No":int(input("Enter The Product Number:")),
            "Product_Name":input("Enter the Product Name:"),
            "Product_type":input("Enter The Product Type:"),
            "Price":int(input("Enter the Price Of the Product:")),
            "Warrenty":input("Enter the Warrenty(in years):"),
            "capacity":input("Enter The Capacity of The Product(in kg):"),
            "Quantity":input("Enter The Quantity Of The Product:"),
            "brand":input("Enter The Brand Of The Product:"),
            "Decription":input("Provide Decription About Product:")
    }
    
    
    print(Product)
   


def add_product():
    try:
        Product_No=int(input("Enter The Product Number:"))
        Product_Name=input("Enter the Product Name:")
        Product_type=input("Enter The Product Type:")
        Price=int(input("Enter the Price Of the Product:"))
        Warrenty=input("Enter the Warrenty(in years):")
        capacity=input("Enter The Capacity of The Product(in kg):")
        Quantity=input("Enter The Quantity Of The Product:")
        brand=input("Enter The Brand Of The Product:")
        Decription=input("Provide Decription About Product:")
        Product1={"Product No":Product_No,"Product Name":Product_Name,"Product Type":Product_type,"Price":Price,"Warrenty":Warrenty,"Quantity":Quantity,"capacity":capacity,"brand":brand,"Decription":Decription}
        Products.append(Product1)
        print("Product has been added successfully")
        check=input("Do you need to verify the Product Details(Y or N):")
        if check.upper()=='yes' or 'y':
            print(Products)
    except ValueError as e:
        print("Exception",e)


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
        Product_No=int(input("Enter The Product Number:"))
        Product_Name=input("Enter the Product Name:")
        Product_type=input("Enter The Product Type:")
        Price=int(input("Enter the Price Of the Product:"))
        Warrenty=input("Enter the Warrenty(in years):")
        capacity=input("Enter The Capacity of The Product(in kg):")
        Quantity=input("Enter The Quantity Of The Product:")
        brand=input("Enter The Brand Of The Product:")
        Decription=input("Provide Decription About Product:")
        Product={"Product No":Product_No,"Product Name":Product_Name,"Product Type":Product_type,"Price":Price,"Warrenty":Warrenty,"Quantity":Quantity,"capacity":capacity,"brand":brand,"Decription":Decription}
        Product[input("Enter the key:")]=input("Enter value:")
        print('')
        Products.append(Product)
        print("Product Status has been Updated")
        check=input("Do you need to verify the Product Details:")
        if check.upper()=='yes' or 'y':
           print(Product)
    except ValueError as e:
        print("Exception:",e)

def visits_product():
    
    no_of_visitors=input("No Of Visitors To The Product:")
    visitstate=input("Do You Want To Know The No Of Visitors For Your Product(Y or N):")
    if visitstate.upper()=='Y' or 'y':
        print("No Of Visitors For Your Product Is:",no_of_visitors)
     


def clear_cart():

    print("\nThe Original Products Details in The List Dictionary Are : ", Products, end = "\n")
    clearState = input("\nDo You Want To Clear The Total Products Details (Y OR N) : ")
    if clearState == 'Yes' or clearState == 'y':
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

def purchase_date():
    
        purchased_date=input("Purchased Date Of Your Product:")
        datestate=input("Do You Want To Know The Purchased Date Of Your Product(Y or N):")
        if datestate.upper()=='yes' or 'y':
            print("Your Purchased Date Of Your Product is:",purchased_date)
        else:
            print("Go Back The Home...")

def return_product():
    returnstate=input("Do You Have The Option To Return The Product(Y or N):")
    if returnstate.upper()=='yes' or 'y':
        print("Yes You can return the product if any problem is there with the product")
    else:
        print("Nope!,Their is no return option available")    

def exchange_product():
    exchangestate=input("Do You Have The Option To Exchange The Product(Y or N):")  
    if exchangestate.upper()=='yes' or 'y':
        print("Yes You can exchange the product with another!")
    else:
        print("Nope!,Their is no exchange facility available in our website")          

def delivery_shopping():
    deliverystate=input("Will You Provide Delivery For The Products(Y or N):")
    if deliverystate.upper()=='yes' or 'y':
       print("Yup,Our Website Provides Free Delivery!")
    else:
        print("Nope!,Free Delivery Is Not Available")   


def main():
    loopstatus=True
    while loopstatus:
        display_cart()
        choice=int(input("Enter your choice:"))
        try:
            if choice==1:
                create_products()
            elif choice==2:
                add_product()
            elif choice==3:
                view_cart()
            elif choice==4:
                edit_cart()
            elif choice==5:
                visits_product()          
            elif choice==6:
                clear_cart()            
            elif choice==7:
                apply_discount()   
            elif choice==8:  
                get_bill() 
            elif choice==9:
                purchase_date()
            elif choice==10:
                return_product()
            elif choice==11: 
                exchange_product()
            elif choice==12:
                delivery_shopping()     
            elif choice==13:    
                loopstatus=False
                print("Exiting from the Shopping Cart..GoodBye!")
                break
            else:
                print("Invalid choice,please enter your choice between[1-13]:")
            continueState=input("\nDo You Want To Continue Again(Y Or N):")
            print(' ')
            if continueState == 'N' or continueState == 'n':
                print("\nYou Requested For Process Termination...Thank You")
                loopstatus=False
        except ValueError:
            print("Please Provide Valid Choice") 

if "_init_"==main():
   main()

