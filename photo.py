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
browser.get("https://academia.srmist.edu.in/#Report:Student_Profile_Report")
browser.switch_to.frame("zohoiam")
login_email=browser.find_element(By.NAME,"LOGIN_ID")
login_email.send_keys('uj8866@srmist.edu.in')
# browser.switch_to.frame("zohoiam")
submit_but = browser.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/form/div[1]/button")
submit_but.click()


sleep(15)

password_field = browser.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/form/div[1]/div[2]/div[2]/input")
password_field.send_keys("C!apton450")
submit_but = browser.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/form/div[1]/button")
submit_but.click()
browser.implicitly_wait(1)
sleep(5)

browser.get("https://academia.srmist.edu.in/#Report:Student_Profile_Report")
photo_holder = browser.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[3]/div[2]/div[2]/div[3]/div[1]/div[1]/div/div[1]/div/div/div/table/tbody/tr/td[4]")
photo_holder.click()
sleep(5)
main_photo = browser.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[3]/div[2]/div[2]/div[3]/div[2]/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div[2]/div[2]/label/a")
main_photo.click()

image_url = "https://previewengine.zoho.com/image/CREATOR/6121375000001147619?cli-msg=eyJzY29wZW5hbWUiOiJzcm1fdW5pdmVyc2l0eSIsImFwcGxpbmtuYW1lIjoiYWNhZGVtaWEtYWNhZGVtaWMtc2VydmljZXMiLCJ2aWV3bGlua25hbWUiOiJTdHVkZW50X1Byb2ZpbGVfUmVwb3J0IiwicmVjb3JkaWQiOiIyNzI3NjQzMDAwMjc3NjA2NTA4IiwiZmllbGRsaW5rbmFtZSI6IllvdXJfUGhvdG8iLCJmaWxlcGF0aCI6IjE2NzQ5NjgyNzc2MTZfVXRzYXZfSmFpc3dhbC5qcGciLCJkaWdlc3RWYWx1ZSI6ImV5SmthV2RsYzNSV1lXeDFaU0k2TVRZNU1UVXhPRFkzT0RVNE9IMCIsImRvd25sb2FkdHlwZSI6ImltYWdlIiwiYXV0aG9yaXplZG1vZHVsZSI6InJlcG9ydCIsImxvZ2luWnVpZCI6IjEwMDUyMjEzMTUxIiwieC1jbGktemFpZCI6IjEwMDAyMjI3MjQ4Iiwic2NvcGVJZCI6IjQ5OTEwODQyIiwiYXBwTGlua05hbWUiOiJhY2FkZW1pYS1hY2FkZW1pYy1zZXJ2aWNlcyIsIngtYXV0aC1wYXRoIjoic3JtX3VuaXZlcnNpdHkvYWNhZGVtaWEtYWNhZGVtaWMtc2VydmljZXMiLCJpc1BvcnRhbCI6dHJ1ZX0="
save_path = "./__pycache__/downloaded_face.jpg"

chrome_options = Options()
chrome_options.add_argument("--headless")  # Run the browser in headless mode (no UI)

browser.get(image_url)
browser.implicitly_wait(10)
image_element = browser.find_element(By.TAG_NAME, "img")
image_src = image_element.get_attribute("src")
response = requests.get(image_src)

with open(save_path, "wb") as f:
        f.write(response.content)
        print(f"Image downloaded successfully to: {save_path}")

sleep(5)