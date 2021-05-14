# Бот для написання коментарів під вказаним постом

from time import sleep
from selenium import webdriver
from random import randint

browser = webdriver.Firefox(executable_path=r'<повний шлях до geckodriver.exe>')
browser.implicitly_wait(5)

browser.get('https://www.instagram.com/')

sleep(2)

username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")

username_input.send_keys("<логін до акаунту>")
password_input.send_keys("<пароль до акаунту>")

login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()

sleep(2)

button = browser.find_element_by_xpath("//button[text()='Не зараз']")
button.click()

sleep(2)

button = browser.find_element_by_xpath("//button[text()='Не зараз']")
button.click()

sleep(2)

browser.get('<посилання на пост>')

sleep(2)

input("Press Enter to start")

comments_text = ["<текст коментаря1>", "<текст коментаря2>"] # варінти коментарів

i = 0
while True:
    if i >= len(comments_text):
        i = 0
    text = comments_text[i]
    i += 1
    try:
        # перехоплення помилки, зв'язаної з захистом від спаму
        comments_input = browser.find_element_by_css_selector("textarea[placeholder='Додайте коментар...']")
        comments_input.click()
        comments_input = browser.find_element_by_css_selector("textarea[placeholder='Додайте коментар...']")
        comments_input.send_keys(text)

        public_button = browser.find_element_by_xpath("//button[@type='submit']")
        public_button.click()
    except Exception:
        try:
            public_button = browser.find_element_by_xpath("//button[@type='submit']")
            public_button.click()
        except Exception:
            pass
    sleep(randint(3, 6)) # випадкова перерва між коментарями (3-6 секунд)
