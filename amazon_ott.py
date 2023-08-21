from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from win10toast_click import ToastNotifier
from plyer import notification

browser = webdriver.Chrome ("D:\old pc\Softwares\chromedriver_win32\chromedriver")
def main():        
    def confirm_otp():
        def otp_done():
            root.destroy()

        root = Tk()
        root.title("CONFIRM YOUR OTP")
        root.geometry("128x128")
        root.config(bg='white')
        button_frame = Frame(root,bg='white')
        button_frame.grid(row=0,column=0)
        otp_image=PhotoImage(file='otp_icon.png')
        otp_button = Button(button_frame,image=otp_image, text="CONFIRM OTP",bd=0,bg='white',activebackground="white",command=otp_done)
        otp_button.pack()
        
        return True
    # Create a tkinter window
    root = Tk()
    root.title("Amazon Billing Date Checker")
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
        root = Tk()
        root.title("Notification Center")
        root.geometry("720x480")
        check_button = Button(root, text="Pay the bills!", command=None,height=400,width=400)
        check_button.grid(row=0,column=0)
        check_button.pack(pady=25)
        root.mainloop()
        
    def display_notifications():
        notification_title ="MESSAGE FROM FAADINEPALI"
        notification_message = "Your AmazonPrime is gonna expire on: " + billing_date_label.cget("text")
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
        browser = webdriver.Chrome("D:\old pc\Softwares\chromedriver_win32\chromedriver")
        browser.implicitly_wait(1)
        browser.get("https://www.primevideo.com/region/in/offers/nonprimehomepage/ref=atv_auth_pre")
        sleep(1)
        def login():
            try:
            
                first_click = browser.find_element(By.CLASS_NAME,"DVPAWebWidgetsUI_Button__prime")
                first_click.click()
                
                username_input = browser.find_element(By.NAME,"email")
                password_input = browser.find_element(By.NAME,"password")
                submit=browser.find_element(By.CLASS_NAME,"a-button-input")
                username_input.send_keys(email)
                password_input.send_keys(password)
                submit.click()
                sleep(5)
                
                return True
            except:
                return False
            
        if login():
            try:
                #_3eGqWR dT7f7i f11d1lkh
                browser.get("https://www.amazon.in/")
                profile_button = browser.find_elements(By.CLASS_NAME,"nav-line-2")[2]
                profile_button.click()
                # sleep(5)
                profile_button = browser.find_elements(By.CLASS_NAME,"a-box-inner")[2].click()
                # sleep(5)
                billingDate = browser.find_elements(By.CLASS_NAME,"mcx-menu-item__heading")[1]
                print(billingDate)
                # index=0
                # for i in billingDate:
                #     print(f'{index} {i.get_attribute("innerHTML")}')
                #     index+=1
                billingDateHTML = billingDate.get_attribute("innerHTML")
                
                billing_date_label.config(text="Your AmazonPrime subscription will end on " + billingDateHTML )
                display_notifications()
            except Exception as e:
                print(e)
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
if __name__ == "__main__":
    main()