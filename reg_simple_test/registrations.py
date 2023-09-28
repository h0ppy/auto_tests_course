from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def registration_page_1():
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
 
    input1 = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
    input1.send_keys("Barak")
    input2 = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
    input2.send_keys("Obama")
    input3 = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
    input3.send_keys("obama@gmail.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    return welcome_text

def registration_page_2():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)
 
    input1 = browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]')
    input1.send_keys("Barak")
    input2 = browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]')
    input2.send_keys("Obama")
    input3 = browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]')
    input3.send_keys("obama@gmail.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    return welcome_text