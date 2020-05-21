import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

messages = [line.replace('\n', '') for line in open("messages.txt", "r")]
for s, i in enumerate(messages):
    print("{}: {}".format(i, s))


'''
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
    messages = [line for line in open("messages.txt", "r")]


browser = None
messages = None

start_whatsapp()
count = 10

for i in range(count):
    text = messages[i % len(messages)]
    text += " Chuttiya"
    el = get_user('Umar Amjad')
    el.click()
    get_message_box().send_keys("YAIN HURT")
    get_message_box().send_keys(Keys.ENTER)

browser.close()
'''
