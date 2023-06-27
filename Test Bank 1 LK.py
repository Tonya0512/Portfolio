from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

s=Service('C:/chromedriver/chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://idemo.bspb.ru/auth?response_type=code&client_id=1&redirect_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fsuccess&prefetch_uri=https%3A%2F%2Fidemo.bspb.ru%2Flogin%2Fprefetch&force_new_session=true")
driver.set_window_size(1544, 1311)
driver.find_element(By.NAME, "username").click()
driver.find_element(By.NAME, "password").click()
driver.find_element(By.ID, "login-button").click()
driver.find_element(By.CSS_SELECTOR, ".resend-text").click()
driver.find_element(By.ID, "login-otp-button").click()
time.sleep(5)
  
