from selenium import webdriver
import time
import pyautogui
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

for x in range(13):
    options = Options()
    options.add_argument("start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get("https://www.instagram.com/")
    time.sleep(5)
    login_user = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
    login_user.send_keys("Your insta username")
    time.sleep(5)
    login_password = driver.find_element(By.XPATH, "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
    login_password.send_keys('Your password')
    login_password.submit()
    time.sleep(5)
    f = open("beemovie", 'r')

    for word in f:
        search_click = driver.find_element(By.XPATH, "/html/body/div[1]/section/nav/div/div/div/div[2]/input")
        search_click.send_keys('#nature')
        time.sleep(15)
        neededelement = driver.find_element(By.XPATH, "/html/body/div/section/nav/div/div/div/div[2]/div/div/div/div/div[1]/a")
        neededelement.click()
        time.sleep(10)
        neededelement2 = driver.find_element(By.XPATH, "/html/body/div/section/main/article/div[2]/div/div/div/a/div/div[2]")
        neededelement2.click()
        time.sleep(10)
        neededelement3 = driver.find_element(By.CLASS_NAME, 'Ypffh')
        neededelement3.click()
        pyautogui.typewrite(word)
        pyautogui.press("enter")
        time.sleep(5)
        driver.refresh()
    driver.quit()
    time.sleep(3600)





