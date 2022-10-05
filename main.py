from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:\\Users\\Administrator\\Documents\\Selenium\\chromedriver.exe")
driver.maximize_window();

#Going to the website.
driver.get("https://10minuteschool.com/auth/login?returnUrl=")
time.sleep(1)

#Changing the language of the website (Bangla to English).
driver.find_element(By.XPATH, '//span[contains(text(),"English")]').click();
time.sleep(1)

#Finding & Filling Username box.
driver.find_element(By.NAME, "username").send_keys("Enter your email")
time.sleep(1.25)

#clicking submit button & moving to next page.
driver.find_element(By.XPATH, '//button[@type="submit"]').click()
time.sleep(1.5)

#Finding & Filling passwor box.
driver.find_element(By.XPATH, "//input[@type='password']").send_keys("Enter password")
time.sleep(1.25)

#clicking submit button & loging in.
driver.find_element(By.XPATH, '//button[@type="submit"]').click()
time.sleep(1.5)

#Finding Dropdown & clicking on it.
driver.find_element(By.XPATH, './/span[@class="icon ng-star-inserted"]').click()
time.sleep(1.5)

#clicking element of Dropdown.
driver.find_element(By.XPATH, '//div[@id="dropdown-user"]//*[contains(text(),"My Courses")]').click()
time.sleep(1.25)

#Finding completed course & clicking on theat.
driver.find_element(By.XPATH, '//div[@class="hover:-translate-y-4 ng-star-inserted"]//img').click()
time.sleep(1.5)

#Looking for coures certificate.
driver.find_element(By.XPATH, '//div[@class="flex gap-6"]//span[contains(text(),"সার্টিফিকেট দেখুন")]').click()
time.sleep(3.5)

#clicking certificate download button.
driver.find_element(By.XPATH, '//div[@class="relative z-[1] pt-6"]//span[contains(text(),"ডাউনলোড সার্টিফিকেট")]').click()
time.sleep(4)

#closing Driver.
driver.close()
