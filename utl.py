# pip install pyshorteners
# pip install pyperclip

import pyshorteners

url = 'https://www.python.org/downloads/'


def shortenurl(url):
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)

short_url = shortenurl(url)
print(short_url)