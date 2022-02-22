# shopping-cart example

# shopping_cart.py
# download the file shopping_cart.py

# This is the shopping cart project for OPIM-243 -- Python
# To run, please create a new environment in order to use third party packages (shopping-env). Please see the requirements.txt file for specific third party packages to install. In order to run the program please input 'python shopping_cart.py' in the terminal once you have entered cd ~/Desktop/shopping-cart

# To use this program please first install all the necessary packages in the requirements.txt file
    # These include python-dotenv and the pandas package for reading csv files into the code 
    # Run pip install -r requirements.txt but make sure directory is the folder where requirements.txt is located

# Before running the program please create a .env file and input the following:
    # TAX_RATE="Desired tax rate"
    # SENDGRID_API_KEY="Please put your sendgrid API Key here which can be found after creating an account"
    # SENDER_ADDRESS="Please put the email of your 'customer' or the desired receipient of the receipt here"
    # SENDGRID_TEMPLATE_ID="Please put the template ID for your desired receipt here. Instructions on how to create this template are below"

# Once you run the code you will be asked whether you want to use your own csv data or the default data. If you would like to use your own data, please first copy the 'default_products.csv' file in 'data' and input your own product names into it. Rename the file "data/products.csv", as this is the file name that the code will draw from for a list of products. 

# In your template on sendgrid, please copy and paste the HTML code below: 
# INSERT HTML CODE HERE -- COULD NOT COMPLETE, WAS LOCKED OUT

