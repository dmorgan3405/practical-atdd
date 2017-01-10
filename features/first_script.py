from selenium import webdriver

if __name__ == '__main__':
    browser = webdriver.Chrome()
    browser.get('http://puppies-app.herokuapp.com')

    browser.close()
