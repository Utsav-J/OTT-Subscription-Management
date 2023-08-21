from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import requests
from win10toast_click import ToastNotifier
from time import sleep
import ott
from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
# from win10toast_click import ToastNotifier
from plyer import notification
from datetime import datetime,timedelta


browser = webdriver.Chrome ("D:\old pc\Softwares\chromedriver_win32\chromedriver")
browser.get("https://www.google.com/")

browser.get("https://www.google.com/images/branding/googlelogo/1x/googlelogo_light_color_272x92dp.png")
browser.implicitly_wait(5)
image_element = browser.find_element(By.TAG_NAME, "img")
image_src = image_element.get_attribute("src")
response = requests.get(image_src)
save_path = "./__pycache__/logo.png"
with open(save_path, "wb") as f:
        f.write(response.content)
        print(f"Image downloaded successfully to: {save_path}")

sleep(5)