from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from auth_data import password, username
import time
import random
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def login(password, username):
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        browser.get('https://www.instagram.com')
        time.sleep(random.randrange(3, 5))

        username_input = browser.find_element(By.NAME, 'username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = browser.find_element(By.NAME, 'password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(10)

        browser.close()
        browser.quit()

    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()


def hashtag_search(password, username, hashtag):
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    try:
        browser.get('https://www.instagram.com')
        time.sleep(random.randrange(3, 5))

        username_input = browser.find_element(By.NAME, 'username')
        username_input.clear()
        username_input.send_keys(username)

        time.sleep(2)

        password_input = browser.find_element(By.NAME, 'password')
        password_input.clear()
        password_input.send_keys(password)

        password_input.send_keys(Keys.ENTER)
        time.sleep(10)

        try:
            browser.get(f'https://www.instagram.com/explore/tags/{hashtag}/')

            time.sleep(4)


            for i in range(1, 31):
                browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(random.randrange(3, 6))


            hrefs = browser.find_elements(By.TAG_NAME, 'a')

            posts_urls = [item.get_attribute('href') for item in hrefs if '/p/' in item.get_attribute('href')]
            print(posts_urls)


#
            for url in posts_urls:
                browser.get(url)
                time.sleep(15)

                like_button = browser.find_element(By.CLASS_NAME, '_aamw')
                like_button.click()
                time.sleep(random.randrange(80, 100))

            browser.close()
            browser.quit()
        except Exception as ex:
            print(ex)
            browser.close()
            browser.quit()

    except Exception as ex:
        print(ex)
        browser.close()
        browser.quit()


hashtag_search(password, username, 'lvivgram')
