# LinuxAcademy-DL

###### Python script to download videos from your LinuxAcademy account for offline viewing
#
#
### Requirements
BeautifulSoup - https://pypi.org/project/beautifulsoup4/
cookies.txt - https://chrome.google.com/webstore/detail/cookiestxt/njabckikapfpffapmjgojcnbfjonfjfg?hl=en

### Usage

> Clone the repo

> Login to LinuxAcademy and visit the course page e.g. https://linuxacademy.com/cp/modules/view/id/287 and with the `cookies.txt` extention installed, click on the icon of the extension and choose `To download cookies for this tab click here`. Copy the downloaded txt file to root of the cloned repo. Make sure that the name of the file is ``cookies.txt``. Repeat when you an encounter exception in downloading the videos (assuming you have an active subscription).

> course_id e.g. https://linuxacademy.com/cp/modules/view/id/287

``` python
>>> python driver.py username password course_id
```

### To-Do
Automate the process for obtaining cookies



