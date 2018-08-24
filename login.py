from selenium import webdriver
from getpass import getpass



# def site_login
#     driver.get("URL")
#     driver.find_element_by_id("ID").send_keys("username")
#     driver.find_element_by_id("ID").send_keys("password")
#     driver.find_element_by_id("submit").click()


print("FACEBOOK LOGIN ")

driver =  webdriver.Chrome()
driver.get("https://www.facebook.com")
user_email=input("Email: ")
user_pass=getpass("password :")
driver.find_element_by_id("email").send_keys(user_email)
driver.find_element_by_id("pass").send_keys(user_pass)
driver.find_element_by_id("loginbutton").click()    