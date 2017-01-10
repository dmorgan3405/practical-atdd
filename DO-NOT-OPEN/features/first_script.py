from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import sys

if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get('http://puppies-app.herokuapp.com')
    browser.find_element(By.CSS_SELECTOR, '[value="View Details"]').click()
    browser.find_element(By.CSS_SELECTOR, '[value="Adopt Me!"]').click()
    browser.find_element(By.CSS_SELECTOR, '[value="Complete the Adoption"]').click()
    browser.find_element(By.ID, 'order_name').send_keys('Doug Morgan')
    browser.find_element(By.ID, 'order_address').send_keys('123 Drury Lane')
    browser.find_element(By.ID, 'order_email').send_keys('dmorgan3405@gmail.com')
    Select(browser.find_element(By.ID, 'order_pay_type')).select_by_visible_text('Credit card')
    browser.find_element(By.CSS_SELECTOR, '[value="Place Order"]').click()
    browser.close()
    sys.exit()
