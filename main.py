from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

serv_obj=Service("C:\Driver\chromedriver-win64\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=serv_obj,options=options)
driver.implicitly_wait(2)
driver.get("https://opensource-demo.orangehrmlive.com/")



driver.find_element(By.NAME,"username").send_keys("Admin")
driver.find_element(By.NAME,"password").send_keys("admin123")
driver.find_element(By.CLASS_NAME,"oxd-button").click()


dashboard=driver.find_element(By.CLASS_NAME,"oxd-text--h6").text
exp_dashboard="Dashboard"

if dashboard==exp_dashboard:
    print("Login Successful")
else:
    print("Login Failed")


# exp_title=


