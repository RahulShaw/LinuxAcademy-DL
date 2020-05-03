# Download videos from Linux Academy / LinuxAcademy-DL

###### Python script to download videos from your LinuxAcademy account for offline viewing
![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)
### Requirements
- Python 3.6 and above
- BeautifulSoup - https://pypi.org/project/beautifulsoup4/
- html5lib - https://pypi.org/project/html5lib/
- Selenium - https://pypi.org/project/selenium/
- ChromeDriver - http://chromedriver.chromium.org/
- youtube_dl - https://pypi.org/project/youtube_dl/
- cookies.txt - https://chrome.google.com/webstore/detail/cookiestxt/njabckikapfpffapmjgojcnbfjonfjfg?hl=en
- FFMpeg - https://www.ffmpeg.org/download.html

### Usage

> Clone the repo

> Run `pip install -r requirements.txt`

> FFmpeg should be installed and available on the path

> Login to LinuxAcademy and visit the course page e.g. https://linuxacademy.com/cp/modules/view/id/287 and with the `cookies.txt` extention installed, click on the icon of the extension and choose `To download cookies for this tab click here`. Copy the downloaded txt file to root of the cloned repo. Make sure that the name of the file is ``cookies.txt``. Repeat when you an encounter exception in downloading the videos (assuming you have an active subscription).

> course_link e.g. https://linuxacademy.com/cp/modules/view/id/287

``` python
>>> python driver.py username password course_link
```
### What's New

 - Now less verbose
 - Minor enhancements and fixes

### To-Do
Automate the process for obtaining cookies
