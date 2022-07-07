'''
Create locators + search strategy

Amazon logo, search by Class, "a-icon a-icon-logo"
Email field, search by ID, "ap_email"
Continue button, search by ID, "continue"
Need help link, search by Class, "a-expander-prompt"
Forgot your password link, search by ID, "auth-fpp-link-bottom"
Other issues with Sign-In link, search by ID, "ap-other-signin-issues-link"
Create your Amazon account button, search by ID, "createAccountSubmit"

Conditions of use link, search by XPATH, //*[@id='legalTextRow']//*[contains(@href, 'nodeId=508088')]
Privacy Notice link, search by XPATH, //*[@id='legalTextRow']//*[contains(@href, 'nodeId=468496')]

'''

# test case
# logged out user opens hello sign in menu
# clicks sign in link on menu
# sign in page appears
# text is typed into email or mobile number field

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome(executable_path='C:/Users/v33ja/Desktop/Careerist/Automation_Course/code/python-selenium-automation/chromedriver.exe')
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/')

# open Hello Sign In
driver.find_element(By.XPATH, "//*[contains(@href, 'signin')]")

# click Sign In link
driver.find_element(By.XPATH, "//*[contains(@href, 'signin')]").click()

# locate email text field
driver.find_element(By.ID, 'ap_email')
sleep(2)

# type text in email text entry
driver.find_element(By.ID, 'ap_email').send_keys('thisistest')
sleep(2)

driver.quit()
