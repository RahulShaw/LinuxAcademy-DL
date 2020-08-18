from __future__ import unicode_literals

import os
import platform
import re
import shutil
import sys
import time

import youtube_dl
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

username = sys.argv[1]
pwd = sys.argv[2]
url = sys.argv[3]

if not (sys.version_info.major == 3 and sys.version_info.minor >= 6):
    print("This script requires Python 3.6 or higher!")
    print("You are using Python {}.{}".format(sys.version_info.major, sys.version_info.minor))
    sys.exit(1)

print("""
    __    _                  ___                  __                           ____  __ 
   / /   (_)___  __  ___  __/   | _________ _____/ /__  ____ ___  __  __      / __ \/ / 
  / /   / / __ \/ / / / |/_/ /| |/ ___/ __ `/ __  / _ \/ __ `__ \/ / / /_____/ / / / /  
 / /___/ / / / / /_/ />  </ ___ / /__/ /_/ / /_/ /  __/ / / / / / /_/ /_____/ /_/ / /___
/_____/_/_/ /_/\__,_/_/|_/_/  |_\___/\__,_/\__,_/\___/_/ /_/ /_/\__, /     /_____/_____/
                                                               /____/                   
""")

if shutil.which('ffmpeg') is None:
    print(
        f'FFmpeg not found. For help, please visit: https://www.google.com/search?q=install%20ffmpeg%20on%20{platform.system()})',
        end='\n\n')
    exit(1)

print("Executing for " + url)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 ' \
             'Safari/537.36 '
headers = {
    'User-Agent': user_agent
}

chrome_options = Options()
chrome_options.add_argument(f'user-agent={user_agent}')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument('--disable-popup-blocking')
chrome_options.add_argument('--disable-logging')
chrome_options.add_argument('--allow-running-insecure-content')
chrome_options.add_argument('--headless')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

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
browser.set_window_size(1366, 768)

browser.get('https://linuxacademy.com/cp/ssologin')
time.sleep(15)

print('* Trying to log in ... *')
user = browser.find_element_by_name('username')
user.send_keys(username)
password = browser.find_element_by_name('password')
password.send_keys(pwd)
password.send_keys(Keys.RETURN)
time.sleep(30)

try:
    logged_in_name = browser.find_element_by_id('navigationUsername')
    if logged_in_name:
        print('\033[92m~ Logged in! ~\033[0m')
except Exception as e:
    raise Exception(' ** Failed to log in. Please check your credentials. **')

print('Getting lesson links...')
browser.get(url)
time.sleep(10)
html = browser.page_source
parsed_html = BeautifulSoup(html, 'html5lib')

urls = []
lessons = []

title = parsed_html.find('div', attrs={'class', 'course-title'}).find('h1').find(text=True, recursive=False)
anchors = parsed_html.find_all('a', attrs={'class', 'syllabus-item'})

print(f'Course name detected as {title}')
print('Enumerating links and sources ...')

for index, anchor in enumerate(anchors):
    if '/course/' in anchor['href']:
        urls.append('https://linuxacademy.com/' + anchor['href'])
        lessons.append(anchor.find('h6').text)
        print(f'Progress: {(index + 1)} of {len(anchors)}', end='\r')
    else:
        pass

if not os.path.exists(title):
    os.makedirs(re.sub('[?/:]', '', title))

browser.close()
browser.quit()

print('Commencing download ...')

if not os.path.exists(os.getcwd() + os.path.sep + 'cookies.txt'):
    print("Cookies.txt not found!")
    exit(1)

try:
    for index, url in enumerate(urls, start=0):
        temp_list = [urls[index]]
        serial = str(index + 1)
        print(f'Downloading: {lessons[index]} ... ', end='', flush=True)
        ydl_opts = {
            'cookiefile': 'cookies.txt',
            'force_generic_extractor': True,
            'outtmpl': os.getcwd() + os.path.sep + title + os.path.sep + serial + '. ' + re.sub('[?/:]', '',
                                                                                                lessons[
                                                                                                    index]) + '.%(ext)s',
            'sleep_interval': 10,
            'retries': 10,
            'allsubtitles': True,
            'verbose': False,
            'quiet': True,
            'writesubtitles': True,
            'no_warnings': True
        }
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download(temp_list)
            temp_list.clear()
            print('\033[92m[Done \u2713]\033[0m')

    print('\n\033[92m** Downloads completed! **\033[0m\n')
except Exception as e:
    print(e)
    print('Downloading failed. Perhaps, the cookies have expired.')
