from ast import Assert, If, Try
import time, os
import xml.etree.ElementTree as ET
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

#os.chdir('../')
#os.getcwd() + "\drivers\chromedriver.exe"
chromeDriverFilePath = "C:\\Users\\Office PC\\Desktop\\Projects\\Automation\\drivers\\chromedriver.exe" 
print(chromeDriverFilePath)

driver = webdriver.Chrome(chromeDriverFilePath)
driver.get("https://www.saucedemo.com/")

# 0. Log into site
loginUserField = driver.find_element(By.ID, "user-name")
loginUserField.send_keys("standard_user")
time.sleep(1)

loginUserPassword = driver.find_element(By.ID, "password")
loginUserPassword.send_keys("secret_sauce")
time.sleep(1)

loginBtn = driver.find_element(By.ID, "login-button")
loginBtn.click()
time.sleep(2)

# 1. Get title and price of backpack
# Need to understand how to return text of a child container as a variable when the parent container does not have a unique identifier
# ** See ANSWER BELOW **
""" Sudo:
take all items on page inside the classname 'inventory_list' and add to array of objects with following structure where 'i' is the number which the item is listed on the page:
inventoryList = [
        i {
            title: driver.find_element(By.CLASS_NAME, 'inventory_item_name').text
            price: driver.find_element(By.CLASS_NAME, 'inventory_item_price').text
        }
    ]
"""

#swagItem = driver.find_element(By.CLASS_NAME, "inventory_item")
#itemPrice = driver.find_element(By.CLASS_NAME, "inventory_item_price")
# print(swagItem.itemPrice)
# for i in swagItem:
#     print(i.text)

#                                 *************** ANSWER ***************
# List of our non Unique elements
swagList = driver.find_elements(By.CLASS_NAME, "inventory_item")

# Variables for item name/price (will use these to validate later)
itemName = ""
itemPrice = 0.00

# Iterate through each item in swagList
for inventoryItem in swagList:

    # Get the name of the item we are iterating through (Notice we aren't using driver.find_element)
    itemNameInList = inventoryItem.find_element(By.CLASS_NAME, "inventory_item_name")

    # TODO: Eventually want to use a variable so we can get the item name and price for anything
    if (itemNameInList.text == "Sauce Labs Backpack"):
        
        # Store name and price in variables
        itemName = itemNameInList.text
        itemPrice = inventoryItem.find_element(By.CLASS_NAME, "inventory_item_price").text

        # Add to cart and break out of loop
        driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
        break

#                          *************** END ANSWER ***************

time.sleep(2)

# 3. Validate "Add to cart" button has updated text to "REMOVE"
swagRemove = driver.find_element(By.ID, "remove-sauce-labs-backpack")
print("swagRemove.text: ", swagRemove.text)
try:
    assert "REMOVE" in swagRemove.text
    print("Add to Cart changed to REMOVE")
except:
    print("Add to Cart did not change as expected. ")
    
time.sleep(1)

# 4. Click shopping cart icon
swagCart = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
swagCart.click()
time.sleep(1)

# 5. Click checkout button
swagCheckOut = driver.find_element(By.ID, "checkout")
swagCheckOut.click()
time.sleep(1)

# 6. Validate shipping info page is shown
swagShippingInfo = driver.find_element(By.CLASS_NAME, "checkout_info")
print("swagShippingInfo.text: ", swagShippingInfo.text)
try:
    assert swagShippingInfo
    print("Page header shows for your information page")
except:
    print("Page header does not show information") 

# 7. Insert shipping info and continue
checkoutFirstName = driver.find_element(By.ID, "first-name")
checkoutFirstName.send_keys("John")
time.sleep(1)

checkoutLastName = driver.find_element(By.ID, "last-name")
checkoutLastName.send_keys("Doe")
time.sleep(1)

checkoutPostalCode = driver.find_element(By.ID, "postal-code")
checkoutPostalCode.send_keys("01234")
time.sleep(1)

checkoutContinue = driver.find_element(By.ID, "continue")
checkoutContinue.click()
time.sleep(1)

# 8. Validate backpack is in cart using previously stored variables
itemNameInCart = driver.find_element(By.CLASS_NAME, "inventory_item_name")
try:
    assert itemNameInCart.text == itemName
    print(itemName + " was found in the cart")
except:
    print("Incorrect item was found in the cart...")

# 9. Validate price using previously stored variable
itemPriceInCart = driver.find_element(By.CLASS_NAME, "inventory_item_price")
try:
    # Check to see if the item price is correct
    assert itemPriceInCart.text == itemPrice
    print(itemPrice + " was found in the cart")
except:
    print("Incorrect item price was found for " + itemName)

# 10. Click finish button
checkoutFinish = driver.find_element(By.ID, "finish")
checkoutFinish.click()
time.sleep(1)

# 11. Validate thank you page appears
checkoutCompleteContainer = driver.find_element(By.ID, "checkout_complete_container")

# 12. Click home button
returnHomeBtn = driver.find_element(By.ID, "back-to-products")
returnHomeBtn.click()
time.sleep(1)

# 13. Log out
burgerMenu = driver.find_element(By.ID, "react-burger-menu-btn")
burgerMenu.click()
time.sleep(1)

logoutBtn = driver.find_element(By.ID, "logout_sidebar_link")
logoutBtn.click()
time.sleep(1)

# 14. Validate back at login screen
# print("loginUserField.text: ", loginUserField.text, "\nloginUserPassword.text: ", loginUserPassword.text, "\nloginBtn.text: ", loginBtn.text)
try:
    assert loginUserField and loginUserPassword and loginBtn
    print("Logon username, password, and logon button loaded successfully")
    
except:
    print("One or all of logon page IDs did not load properly") 

# Close window when script is complete
driver.close()