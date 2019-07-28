from __future__ import unicode_literals
import os
import platform
import re
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import youtube_dl

username = sys.argv[1]
pwd = sys.argv[2]
url = sys.argv[3]

print("Requesting download of " + url)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 ' \
             'Safari/537.36 '
headers = {
    'User-Agent': user_agent
}

chrome_options = Options()
chrome_options.add_argument('user-agent={user_agent}')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-popup-blocking')
chrome_options.add_argument('--disable-logging')
chrome_options.add_argument('--allow-running-insecure-content')

if platform.system() == 'Linux':
    if os.path.exists("/usr/bin/chromedriver"):
        browser = webdriver.Chrome(executable_path="/usr/bin/chromedriver",
                                   options=chrome_options)
    else:
        print("Chromedriver not found; expected path '/usr/bin/chromedriver'")
        exit(1)
else:
    if os.path.exists("C:/ChromeDriver/chromedriver.exe"):
        browser = webdriver.Chrome(executable_path="C:/ChromeDriver/chromedriver.exe",
                                   options=chrome_options)
    else:
        print("Chromedriver not found; expected path 'C:/ChromeDriver/chromedriver.exe'")
        exit(1)


browser.set_page_load_timeout(10000)
browser.maximize_window()
browser.get("https://linuxacademy.com/")

link = browser.find_element_by_partial_link_text('Log In')
link.click()

print("Sleeping for 15 seconds..")
time.sleep(15)

print("Attempting to login..")
user = browser.find_element_by_name('username')
user.send_keys(username)
password = browser.find_element_by_name('password')
password.send_keys(pwd)
password.send_keys(Keys.RETURN)
time.sleep(30)

try:
    logged_in_name = browser.find_element_by_id('navigationUsername')
    if logged_in_name:
        print("Login successful...")
except Exception as e:
    print("Login failed...\nExiting now!")
    exit(1)


print("Getting lesson links...")
browser.get(url)
time.sleep(10)
html = browser.page_source
parsed_html = BeautifulSoup(html, 'html5lib')

urls = []
lessons = []

title = parsed_html.find('span', attrs={'class', 'course-title'}).text
anchors = parsed_html.find_all('a', attrs={'class', 'syllabus-item'})

for anchor in anchors:
    if '/course/' in anchor['href']:
        urls.append('https://linuxacademy.com/' + anchor['href'])
        lessons.append(anchor.find('h6').text)
    else:
        pass

if not os.path.exists(title):
    os.makedirs(re.sub('[?/:]', '', title))

browser.close()
browser.quit()

print("Starting download...")

if not os.path.exists(os.getcwd() + "/cookies.txt"):
    print("Cookies.txt not found!")
    exit(1)

try:
    for index, url in enumerate(urls, start=0):
        temp_list = [urls[index]]
        serial = str(index + 1)
        ydl_opts = {'cookiefile': 'cookies.txt', 'force_generic_extractor': True,
                    'outtmpl': os.getcwd() + '/' + title + "/" + serial + '. ' + re.sub('[?/:]', '',
                                                                                          lessons[index]) + '.%(ext)s',
                    'sleep_interval': 15, 'retries': 10}
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(temp_list)
            temp_list.clear()

    print("Downloads completed!")
except Exception as e:
    print(e)
    print("Downloading failed. Perhaps, the cookies have expired.")
