#starting a Selenium webdriver to pop up a  real Firefox browser window
from selenium import webdriver

#using it to open up a webpage which we are expecting to be served from the local PC
browser = webdriver.Firefox()
browser.get('http://localhost:8000')

#checking (making a test assertion) that the page has the word "Django" in its title
assert 'Django' in browser.title