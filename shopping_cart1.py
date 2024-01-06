"""
Project Name: Shopping Cart project Using List and Dictionaries and Exception Handling
Developer   : Bindu
Date        : 2023-12-26
Description : In this project we are Capturing the Activities of the Products like Add To Cart,View Cart,Edit Cart etc.
                1.Creating User 
                2.Login into the app
                3.Create Products
                4.Add To Cart
                5.View Cart
                6.Edit Cart 
                7.No of visitors to the product
                8.Clear Cart
                9.Apply Discount
                10.Generate the Bill
                11.Purchased date of the product
                12.Return The Product
                13.Exchange The Product
                14.Delivery
                15.Exit The Shopping Cart

Version     : v1.0

"""

global products
products=[]
def display_cart():
    print("="*50)
    print("\t******Shopping Cart*******")
    print("="*50)
    print("1.Creating User")
    print("2.Login To The App")
    print("3.Create Products")
    print("4.Add Task")
    print("5.View Tasks")
    print("6.Edit Cart")
    print("7.No Of Visitors To The Product")
    print("8.Clear Cart")
    print("9.Apply The Discount")
    print("10.Generate The Bill")
    print("11.Purchased Date Of The Product")
    print("12.Return The Product")
    print("13.Exchange the product")
    print("14.Delivery")
    print("15.Exit from the Shopping Cart")
    print("-"*50)


def create_user():
    
    user_details={
        "FullName"       :    input("Enter Your Full Name:"),
        "EmailAddress"   :    input("Enter Email Address:"),
        "UserName"       :    input("Enter The User Name:"),
        "Password"       :    input("Enter Unique Password:"),
        "DateOfBirth"    :    input("Enter Date Of Birth:"),
        'userprofile'    :   {
            "profile"    :{"Bio":input("Enter Your Bio:"),
                           "Preferences":input("Enter Your Preferences:")},
        
        'ShippingAddress' :  {
               "Address" :  {"D/NO"   :input("Enter Your Door NO:"),
                            "name"    :input("Enter Your Name:"),
                            "street"  :input("Enter Street Name:"),
                            "city"    :input("Enter Your City:"),
                            "pincode" :input("Enter Your Pin Code:"),
                            "mobileno":int(input("Enter Your Mobile Number:")),
                            "country" :input("Enter Your Country Name:")}
                            
            
        }                 
    }
    }
    print(' ')
    verification_state=input("Do You Want To Verify Your Email Again(Y or N):")
    if verification_state.lower()=='yes' or verification_state.lower()=='y':
        print("You Will Receive a verification email with a link to click.") 
    else:
        print("Nope,Dont Want To Verify The Email..")    


    print(' ')
    print("User Exists In Our Website,So You Are Allowed To DO Shopping",user_details)
    print(' ')
    exitstate=input("Do You Want Do Shopping In Our Website (Yes or No):")
    if exitstate.lower()=='yes' or exitstate.lower()=='y':
        print("Yup,You Have A Account In Our Website,You Are Allowed To DO Shopping!")
        print("If You DO Shopping You Will Get A Discount Along With The Bill...")
        print(' ')
        apply_discount()
        generate_bill()
    else:
        print(products)
        print("You Are Allowed For Shopping But You Dont Get Bill...")    



def login_app():

    try:
        login_details={
        "UserName"       :    input("Enter The User Name:"),
        "EmailAddress"   :    input("Enter Email Address:"),
        "Password"       :    input("Enter Unique Password:"),
        }
        print(' ')
        print("You Have Login Successfully Into The Website...",login_details)
        continuestate1=input("Do You Want TO Continue The Shopping(Y or N):")
        if continuestate1.lower()=='yes' or continuestate1.lower()=='y':  
            print("Welcome To Our Website....")
        else:
            print("Wrong Password,Please Check The Password...")    

    except ValueError as e:
        print("Exception",e)


def create_products():
   
    products = [
        {
            'Product1': {
                "ProdName":input("Enter the ProductName1:"),
                "Product_type":input("Enter The Product Type:"),
                "Price":int(input("Enter the Price Of the Product:")),
                "Warrenty":input("Enter the Warrenty(in years):"),
                "capacity":input("Enter The Capacity of The Product(in kg):"),
                "Brand":input("Enter The Brand Of The Product:"),
                "Description":input("Provide Decription About Product:")
        }
    },
    {
            'Product2': {
                "ProdName":input("Enter the ProductName2:"),
                "Product_type":input("Enter The Product Type:"),
                "Price":int(input("Enter the Price Of the Product:")),
                "Warrenty":input("Enter the Warrenty(in years):"),
                "capacity":input("Enter The Capacity of The Product(in kg):"),
                "Brand":input("Enter The Brand Of The Product:"),
                "Description":input("Provide Description About Product:")
        }
    },
]
    print(products) 


def add_product():
    try:
        ProdName=input("Enter the ProductName3:")
        Product_type=input("Enter The Product Type:")
        Price=int(input("Enter the Price Of the Product:"))
        Warrenty=input("Enter the Warrenty(in years):")
        capacity=input("Enter The Capacity of The Product(in kg):")
        brand=input("Enter The Brand Of The Product:")
        Description=input("Provide Decription About Product:")
        Product1={"ProdName3":ProdName,"Product Type":Product_type,"Price":Price,"Warrenty":Warrenty,"capacity":capacity,"brand":brand,"Description":Description}
        products.append(Product1)
        print("Product has been added successfully")
        check=input("Do you need to verify the Product Details(Y or N):")
        if check.lower()=='yes' or check.lower()=='y':
            print(products)
        else:
            print("I Dont want to verify the Product Details")    

    except ValueError as e:
        print("Exception",e)


def view_cart():
    i=1
    for pro in products:
            print("-----------------------------")
            print(pro)
            print("-----------------------------")
            for key,value in pro.items():
                print(f"{key}:{value}")
    i=i+1
    
   


def edit_cart():
    
    try:
        ProdName=input("Enter the ProductName4:")
        Product_type=input("Enter The Product Type:")
        Price=int(input("Enter the Price Of the Product:"))
        Warrenty=input("Enter the Warrenty(in years):")
        capacity=input("Enter The Capacity of The Product(in kg):")
        brand=input("Enter The Brand Of The Product:")
        Description=input("Provide Decription About Product:")
        Product={"ProdName4":ProdName,"Product Type":Product_type,"Price":Price,"Warrenty":Warrenty,"capacity":capacity,"brand":brand,"Description":Description}
        Product[input("Enter the key:")]=input("Enter value:")
        print('')
        products.append(Product)
        print("Product Status has been Updated")
        check=input("Do you need to verify the Product Details:")
        if check.lower()=='yes' or check.lower()=='y':
           print(Product)
        else:
            print("I Dont want to verify the Product Details")    
    except ValueError as e:
        print("Exception:",e)

def visits_product():
    
    no_of_visitors=input("No Of Visitors To The Product:")
    visitstate=input("Do You Want To Know The No Of Visitors For Your Product(Y or N):")
    if visitstate.lower()=='yes' or visitstate.lower()=='y':
        print("No Of Visitors For Your Product Is:",no_of_visitors)
    else:
        print("Nope,Dont want to know about the visitors to the product")    


    
def clear_cart():

    print("\nThe Original Products Details in The List Dictionary Are : ", products, end = "\n")
    clearState = input("\nDo You Want To Clear The Total Products Details (Y OR N) : ")
    if clearState.lower()=='yes' or clearState.lower()=='y':
        products.clear()
        print("\nThe Elements After Clearing Are : ", products, end = "\n")
    else:
       print("Nope,Dont want to clear the products...")


def apply_discount():
    print("You Are A User In Our Website,So We Are Giving A Discount...")
    try:    
        Bill=int(input("Enter Total Bill Of The Product:"))
        discount=int(input("Enter The Discount Percentage On Total Bill:"))
        discountstate=input("Do You Want To Apply Discount To The Total Bill(Y or N):")
        if discountstate.lower()=="yes" or discountstate.lower()=='y':
           result=Bill-(Bill*discount/100)
           print("Discount Is Applied To The Bill:",result)
        else:
            print("Nope,I DOnt Want A Discount....")   
    except ValueError as e:
        print("Exception:",e)


def generate_bill():
    print(' ')
    print("You Are A User In Our Website,So We Are Generating A Bill...")
    try:   
        Bill=int(input("Enter Total Bill Of The Product:"))
        discount=int(input("Enter The Discount Percentage On Total Bill:"))
        generatestate=input("Do You Want To Generate Bill After Applying Discount(Y or N):")
        if generatestate.lower()=='yes' or generatestate.lower()=='y':
          result=Bill-(Bill*discount/100)
          print("Your Total Bill is:",result)
        else:
          print("Thank you For Shopping In Our Website......")
    except ValueError as e:
        print("Exception:",e)


def purchase_date():
    
        purchased_date=input("Purchased Date Of Your Product:")
        datestate=input("Do You Want To Know The Purchased Date Of Your Product(Y or N):")
        if datestate.lower()=='yes' or datestate.lower()=='y':
            print("Your Purchased Date Of Your Product is:",purchased_date)
        else:
            print("Go Back The Home...")

def return_product():
    returnstate=input("Do You Have The Option To Return The Product(Y or N):")
    if returnstate.lower()=='yes' or returnstate.lower()=='y':
        print("Yes You can return the product if any problem is there with the product")
    else:
        print("Nope!,Their is no return option available")    

def exchange_product():
    exchangestate=input("Do You Have The Option To Exchange The Product(Y or N):")  
    if exchangestate.lower()=='yes' or exchangestate.lower()=='y':
        print("Yes You can exchange the product with another!")
    else:
        print("Nope!,Their is no exchange facility available in our website")          

def delivery_shopping():
    deliverystate=input("Will You Provide Delivery For The Products(Y or N):")
    if deliverystate.lower()=='yes' or deliverystate.lower()=='y':
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
                create_user() 
            elif choice==2:
                login_app()
            elif choice==3:
                create_products()
            elif choice==4:
                add_product()
            elif choice==5:   
                view_cart()      
            elif choice==6:
                edit_cart()            
            elif choice==7:  
                visits_product()
            elif choice==8: 
                clear_cart()
            elif choice==9:
                apply_discount()
            elif choice==10:
                generate_bill()
            elif choice==11: 
                purchase_date() 
            elif choice==12:
                return_product()   
            elif choice==13:
                exchange_product() 
            elif choice==14:
                delivery_shopping()  
            elif choice==15:    
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

