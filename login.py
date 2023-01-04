#imports selenium (pip install selenium if not installed)
from time import sleep
from selenium import webdriver

#insert path to the chromedriver
#must change adapt to your chromedriver path
driver = webdriver.Chrome('/usr/local/bin/chromedriver')

#open up stackoverflow.com
driver.get("https://stackoverflow.com")

#finds login button
login_button = driver.find_element_by_xpath('/html/body/header/div/ol[2]/li[2]/a[1]')

#clicks login button
login_button.click()

#provides time to page to login before proceeding 
sleep(3)

#finds username entry field
username = driver.find_element_by_xpath('//*[@id="email"]')

#enters your username
username.send_keys("your email entered here")

#finds password entry field
password = driver.find_element_by_xpath('//*[@id="password"]')

#enters your password
password.send_keys("your password entered here")

#clicks submit to finsih logging in
driver.find_element_by_xpath('//*[@id="submit-button"]').click()
