import os
from page_object import Browser

os.environ['PAGE_OBJECT_BASE_URL'] = 'https://puppies-app.herokuapp.com/'

browser = Browser.selenium_browser()


def after_all(context):
    browser.close()
