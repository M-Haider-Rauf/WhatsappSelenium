import selenium
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def get_user(name):
    while True:
        try:
            user = browser.find_element_by_xpath("//span[@title='{}']".format(name))
            return user
        except:
            continue


def get_message_box():
    global browser
    while True:
        try:
            box = browser.find_element_by_xpath(".//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
            return box
        except:
            continue

def start_whatsapp():
    global browser
    browser = webdriver.Firefox()
    browser.get("https://web.whatsapp.com/")
    global messages
    messages = [line.replace('\n', '') for line in open("messages.txt", "r")]


browser = None
messages = None

start_whatsapp()
spam_count = 20

ran_gen = random.Random()

for i in range(spam_count):
    text = messages[ran_gen.randint(0, len(messages) - 1)]
    get_user('mama').click()
    get_message_box().send_keys(text)
    get_message_box().send_keys(Keys.ENTER)

browser.close()
