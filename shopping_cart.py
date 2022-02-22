#shopping-cart.py
from datetime import datetime
import os

# this is the "my-secure-project/my_script.py" file...
import os
import pandas as pd
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

load_dotenv()


# ... where they can be accessed / read via the os module as usual:
tax = float(os.getenv("TAX_RATE"))
#print(tax) # for testing

decision = input("If you would like to use your csv file for products, input 'csv' here. If you would like to use the default list, input 'list'.")
if decision=="csv":
    from pandas import read_csv
    csv_filepath = os.path.join(os.path.dirname(__file__), "data", "products.csv")
    x = read_csv(csv_filepath)
    products = {}
    products = pd.read_csv("products.csv", header=1,index_col=1,squeeze=True).to_dict()

else:
    products = [
        {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
        {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
        {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
        {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
        {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
        {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
        {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
        {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
        {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
        {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
        {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
        {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
        {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
        {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
        {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
        {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
        {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
        {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
        {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
        {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
    ] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


# TODO: write some Python code here to produce the desired output

total_price = 0 
product_ids = []
matching_products = []
valid_ids = []
# ASK FOR USER INPUT
player_name = input("Please enter your name here! ")
store_name = (str.title(player_name)+"'s Grocery Store")
# DATE TIME SETUP: 
now = datetime.now()
dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
for i in products:
    valid_ids.append(str(i["id"])) 


print("Welcome to "+ store_name + "! When you are ready to checkout please enter 'DONE' instead of a product identifier. ")

product_ids = []
while True: 
    product_id = input("Please input a product indentifier between 1 and 20. ") #> "9" (string)
    #> "DONE"
    if product_id == "DONE":
        break
    elif product_id in valid_ids:
        # matching_products = [p for p in products if str(p["id"]) == str(product_id)]
        # matching_product = matching_products[0]
        # total_price = total_price + matching_product["price"]
        # print("SELECTED PRODUCT: " + str(matching_product["name"]) + " " + str(matching_product["price"]))
        product_ids.append(product_id)
    else:
        print("That was an invalid product ID. Please try again!")


# INFO DISPLAY / OUTPUT

# print(selected_ids)
for product_id in product_ids:
    matching_products = [p for p in products if str(p["id"]) == str(product_id)]
    matching_product = matching_products[0]
    total_price = total_price + matching_product["price"]
    # print("SELECTED PRODUCT: " + str(matching_product["name"]) + " " + str(matching_product["price"]))


#FORMATTING AND PRINTING RECEIPT
print("---------------------------------")
print(str.upper(store_name))
print(str.upper("WWW."+player_name+"S-GROCERY-STORE.COM"))
print("---------------------------------")
print("CHECKOUT AT: "+dt_string)
print("---------------------------------")
print("SELECTED PRODUCTS:")
for product_id in product_ids:
    matching_products = [p for p in products if str(p["id"]) == str(product_id)]
    matching_product = matching_products[0]
    print("... " + str(matching_product["name"]) + " " + "("+str(to_usd(matching_product["price"])+")"))
print("---------------------------------")

print("SUBTOTAL: " + str(to_usd(total_price))) #Format as USD!
    # return f"${total_price:,.2f}" #> $12,000.71

tax_value = total_price*tax #should be float from env variable
print("TAX: "+(str(to_usd(tax_value))))
total = tax_value + total_price
print("TOTAL: "+(str(to_usd(total))))
print("---------------------------------")
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")
email = input("Would the customer like an email receipt as well? Please input 'y' or 'n'. ")

if email=="n":
    print("Thank you, no receipt will be sent! Come again soon!")
    quit
else:
    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
    SENDGRID_TEMPLATE_ID = os.getenv("SENDGRID_TEMPLATE_ID", default="OOPS, please set env var called 'SENDGRID_TEMPLATE_ID'")
    SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")

    # this must match the test data structure
    template_data = {
        "subtotal_price_usd": str(to_usd(total_price)),
        "tax_usd": str(to_usd(tax_value)),
        "total_price_usd": str(to_usd(total)),
        "date": now.strftime("%m/%d/%Y"),
        "time":now.strftime("%H:%M:%S"),
        "products": "hello"
    
    } 
    # or construct this dictionary dynamically based on the results of some other process :-D

    client = SendGridAPIClient(SENDGRID_API_KEY)
    #print("CLIENT:", type(client))

    message = Mail(from_email=SENDER_ADDRESS, to_emails=SENDER_ADDRESS)
    message.template_id = SENDGRID_TEMPLATE_ID
    message.dynamic_template_data = template_data
    #print("MESSAGE:", type(message))

    try:
        response = client.send(message)
        print("RESPONSE:", type(response))
        print(response.status_code)
        print(response.body)
        print(response.headers)

    except Exception as err:
       print(type(err))
       print(err)

    print("Receipt sent! Thanks again and come again soon!")

