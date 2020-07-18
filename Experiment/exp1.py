# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 12:30:46 2020

@author: hp
"""

from time import sleep
from selenium import webdriver
class LoginPage:
    def __init__(self,browser):
        self.browser = browser
        
    def login(self,username,password):
        username_input = self.browser.find_element_by_css_selector("input[name='username']")  #find username input by CSS
        password_input = self.browser.find_element_by_css_selector("input[name='password']")  #find password input by CSS
        username_input.send_keys("ayush_brainbox_goel")    #enter your username 
        password_input.send_keys("devil123@@##")         #enter your password
        login_button = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]') #find the login button by xpath
        login_button.click()                        #click the login button
        sleep(10)  #this line provides the timer upto which the browser will open the site
        
class HomePage:
    def __init__(self,browser):
        self.browser = browser
        self.browser.get('https://www.instagram.com/')
        
    def go_to_login_page(self):
        self.browser.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input')
        sleep(5)
        return LoginPage(self.browser)
    
    
browser = webdriver.Chrome()
browser.implicitly_wait(5)

home_page = HomePage(browser)
login_page = home_page.go_to_login_page()
login_page.login("ayush_braibbox_goel", "devil123@@##")

#browser.close()