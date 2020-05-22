import selenium
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# get the contact html element with name 'name'
def get_contact(name):
    while True:
        try:
            user = browser.find_element_by_xpath("//span[@title='{}']".format(name))
            return user
        except:
            continue


# get the message input box
def get_message_box():
    global browser
    while True:
        try:
            box = browser.find_element_by_xpath(".//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
            return box
        except:
            continue


# init the driver and load all messages from file
def init_script():
    global browser
    browser = webdriver.Firefox()
    browser.get("https://web.whatsapp.com/")  # whatsapp web url
    global messages
    # load each line from file in list, strip newline characters
    messages = [line.replace('\n', '') for line in open("messages.txt", "r")]


browser = None
messages = None

init_script()
spam_count = 20  # number of messages to send

ran_gen = random.Random()

for i in range(spam_count):
    text = messages[ran_gen.randint(0, len(messages) - 1)]  # choose a random message
    get_contact('mama').click()  # go to contact
    get_message_box().send_keys(text)  # copy message
    get_message_box().send_keys(Keys.ENTER)  # press ENTER... done!

browser.close()
