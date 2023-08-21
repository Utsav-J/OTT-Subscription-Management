from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from win10toast_click import ToastNotifier
from plyer import notification
from datetime import datetime,timedelta

browser = webdriver.Chrome ("D:\old pc\Softwares\chromedriver_win32\chromedriver")

def main():
        
    # Create a tkinter window
    root = Tk()
    root.title("Netflix Billing Date Checker")  

    # Create a label and entry for the email input
    email_label = Label(root, text="Email:")
    # email_label.grid(row=0,column=0)
    email_label.pack()
    email_entry = Entry(root)
    email_entry.pack()

    # Create a label and entry for the password input
    password_label = Label(root, text="Password:")
    # email_label.grid(row=2,column=0)
    password_label.pack()
    password_entry = Entry(root, show="*")
    password_entry.pack()

    def show_the_payment_options():
        # root = Tk()
        # root.title("Notification Center")
        # root.geometry("720x480")
        # check_button = Button(root, text="Pay the bills!", command=None)
        # # check_button.grid(row=3,column=0)
        # check_button.pack(pady=25)
        # root.mainloop()
        browser.get("https://www.netflix.com/YourAccount")

    def display_notifications():
        notification_title ="NETFLIX ALERT- FaadiNepali"
        notification_message = billing_date_label.cget("text")
        
        toaster = ToastNotifier()
        toaster.show_toast(
            notification_title,
            notification_message,
            duration=5,
            threaded=True,
            callback_on_click=show_the_payment_options
        )


    # Create a function to check the billing date
    def check_billing_date():
        # Get the email and password from the input fields
        email = email_entry.get()
        password = password_entry.get()

        # Use Selenium to log in to Netflix and get the billing date
        browser.implicitly_wait(1)
        browser.get("https://www.netflix.com/in/login")
        sleep(1)
        def login():    
            try:
                username_input = browser.find_element(By.NAME,"userLoginId")
                password_input = browser.find_element(By.NAME,"password")
                submit=browser.find_element(By.CLASS_NAME,"login-button")
                username_input.send_keys(email)
                password_input.send_keys(password)
                submit.click()
                acc=browser.find_element(By.CLASS_NAME,"profile-link")
                acc.click()
                return True
            except:
                return False
            
        if login():
            try:
                browser.get('https://www.netflix.com/YourAccount')
                billingDate =  browser.find_elements(By.CLASS_NAME,"account-section-item")[8]
                billingDateHTML = billingDate.get_attribute("innerHTML")
                billing_date_label.config(text=billingDateHTML)
                display_notifications()
            except Exception:
                billing_date_label.config(text="An error occurred while getting your billing date.")
        # browser.quit()

    # Create a button to check the billing date
    check_button = Button(root, text="Check Billing Date", command=check_billing_date)
    # check_button.grid(row=3,column=0)
    check_button.pack()

    # Create a label to display the billing date
    billing_date_label = Label(root)
    billing_date_label.pack()
    # Run the tkinter window
    root.mainloop()