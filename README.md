# Download videos from Linux Academy / LinuxAcademy-DL

###### Python script to download videos from your LinuxAcademy account for offline viewing
![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)

![LinuxAcademy-DL](https://i.imgur.com/RBPjtsv.png)

### Requirements
- Python 3.6 and above
- BeautifulSoup - https://pypi.org/project/beautifulsoup4/
- html5lib - https://pypi.org/project/html5lib/
- Selenium - https://pypi.org/project/selenium/
- ChromeDriver - http://chromedriver.chromium.org/
- youtube_dl - https://pypi.org/project/youtube_dl/
- Get cookies.txt - https://bit.ly/GoogleChrome-GetCookiesTxt
- FFMpeg - https://www.ffmpeg.org/download.html

### Usage

> Clone the repo

> Run `pip install -r requirements.txt`

> FFmpeg should be installed and available on the path

> Login to LinuxAcademy and visit the course page e.g. https://linuxacademy.com/cp/modules/view/id/287 and with the `Get cookies.txt` extension installed, click on the icon of the extension and click on `Export`. 

![Get cookies.txt](https://i.imgur.com/BND0mvs.png)

> Rename the downloaded `linuxacademy.com_cookies.txt` file to `cookies.txt` and copy it to root of the cloned repo. Make sure that the name of the file is ``cookies.txt``. Repeat when you encounter an exception while downloading the videos (assuming you have an active subscription).

> course_link e.g. https://linuxacademy.com/cp/modules/view/id/287

``` python
>>> python driver.py username password course_link
```
### What's New

 - Now less verbose
 - Minor enhancements and fixes

### To-Do
Automate the process for obtaining cookies
